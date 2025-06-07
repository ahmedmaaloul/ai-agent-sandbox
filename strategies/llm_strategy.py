# strategies/llm_strategy.py
import os, json
from dotenv import load_dotenv
from google import genai

# ------------------------------------------------------------------ #
# 1) Initialise client --------------------------------------------- #
# ------------------------------------------------------------------ #
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
if not api_key:
    raise EnvironmentError("Add GOOGLE_API_KEY or GEMINI_API_KEY to your .env")

client = genai.Client(api_key=api_key)           # single, reusable client


# ------------------------------------------------------------------ #
# 2) Strategy ------------------------------------------------------ #
# ------------------------------------------------------------------ #
class LLMStrategy:
    """
    Uses Gemini to decide which tool the agent should call next.
    Always returns a dict like {"tool": "...", "args": {...}}.
    """

    def __init__(self, model_name: str = "gemini-2.0-flash"):
        self.model = model_name

    # ------------------------------------------------------------------ #
    def plan(self, task: str, tools: list[str], context: list[tuple[str, str]]):
        # ---------- Build the prompt ---------- #
        tool_list = ", ".join(tools)
        context_summary = (
            "\n".join(f"{i + 1}. {t} -> {r}" for i, (t, r) in enumerate(context))
            or "None so far"
        )

        system_prompt = (
            "You are a planning module inside an autonomous agent sandbox. "
            "Choose exactly ONE tool from the provided list and return ONLY valid JSON."
        )

        user_prompt = (
            f"Available tools: {tool_list}\n"
            f"Task: {task}\n"
            f"Recent context:\n{context_summary}\n\n"
            "Return JSON like:\n"
            '{"tool": "web_search", "args": {"query": "..."}}\n'
        )

        # ---------- Call Gemini ---------- #
        result = client.models.generate_content(
            model=self.model,
            contents=user_prompt,
            config=genai.types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.2),
        )
        # ---------- Clean & parse response ---------- #
        raw = result.text.strip()

        # ✅ Handle ```json code block formatting
        if raw.startswith("```"):
            raw = raw.lstrip("`json").strip("`").strip()

        try:
            return json.loads(raw)
        except json.JSONDecodeError as e:
            print("⚠️  JSON parse failed, defaulting to web_search:", e, "\nRaw:", raw)
            return {"tool": "web_search", "args": {"query": task}}