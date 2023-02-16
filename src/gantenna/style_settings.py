import torch
from gantenna import DEVICE

class StyleSettings:
    """A class with settings for styling algorithm
    accepts texts and in future accepts images too
    
    can be used for setting full picture style or small picture style"""
    def __init__(self):
        self.positive_prompts=[]
        self.negative_prompts=[]
    def like(self,*texts):
        self.positive_prompts.extend(texts)
    def far_from(self,*texts):
        self.negative_prompts.extend(texts)
    def make_embeds(self, clip, clip_processor):
        positive_embeds=self._embeds_from_text_array(self.positive_prompts,clip,clip_processor)
        negative_embeds=self._embeds_from_text_array(self.negative_prompts,clip,clip_processor)
        return positive_embeds, negative_embeds
    @staticmethod
    def _embeds_from_text_array(text_array, clip, clip_processor):
        with torch.no_grad():
                text_tokens= clip_processor(text_array)
                text_features=clip.encode_text(text_tokens['input_ids'].to(DEVICE)).to(DEVICE)
                text_latents = text_features / text_features.norm(dim=-1, keepdim=True)
                return text_latents       
