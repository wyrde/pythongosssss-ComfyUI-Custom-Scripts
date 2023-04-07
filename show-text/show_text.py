# by pythongossssss
# https://github.com/pythongosssss/ComfyUI-Custom-Scripts/

class ShowText:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "text": ("STRING", {"forceInput": True}),
        }}

    RETURN_TYPES = ("STRING",)
    FUNCTION = "notify"
    OUTPUT_NODE = True

    CATEGORY = "pgos/utils"

    def notify(self, text):   
        return {"ui": { "text": text }, "result": (text,)}


NODE_CLASS_MAPPINGS = {
    "ShowText (pgos)": ShowText,
}