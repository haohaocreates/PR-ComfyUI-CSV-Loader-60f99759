import os
import re
import folder_paths

#ARTISTS

class ArtistsCSVLoader:
    """
    Loads csv file with artists. For migration purposes from automatic11111 webui.
    """
    
    @staticmethod
    def load_artists_csv(artists_path: str):
        """Loads csv file with artists. It has only one column.
        Ignore the first row (header).
        positive_prompt are strings separated by comma. Each string is a prompt.
        negative_prompt are strings separated by comma. Each string is a prompt.

        Returns:
            list: List of artists. Each style is a dict with keys: style_name and value: [positive_prompt, negative_prompt]
        """
        artists = {"Error loading artists.csv, check the console": ["",""]}
        if not os.path.exists(artists_path):
            print(f"""Error. No artists.csv found. Put your artists.csv in the root directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """)
            return artists
        try:
            with open(artists_path, "r", encoding="utf-8") as f:    
                artists = [[x.replace('"', '').replace('\n','') for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)] for line in f.readlines()[1:]]
                artists = {x[0]: [x[1],x[2]] for x in artists}
        except Exception as e:
            print(f"""Error loading artists.csv. Make sure it is in the root directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """)
        return artists
        
    @classmethod
    def INPUT_TYPES(cls):
        cls.artists_csv = cls.load_artists_csv(os.path.join(folder_paths.base_path, "custom_nodes\\ComfyUI-CSV_Loader\\CSV\\artists.csv"))
        return {
            "required": {
                "artists": (list(cls.artists_csv.keys()),),
            },
                                
        }

    RETURN_TYPES = ("STRING","STRING")
    RETURN_NAMES = ("positive prompt", "negative prompt")
    FUNCTION = "execute"
    CATEGORY = "CSV Loaders"   

    def execute(self, artists):
            return (self.artists_csv[artists][0], self.artists_csv[artists][1])


#ARTMOVEMENTS

class ArtmovementsCSVLoader:
    """
    Loads csv file with artmovements. For migration purposes from automatic11111 webui.
    """
    
    @staticmethod
    def load_artmovements_csv(artmovements_path: str):
        """Loads csv file with artmovements. It has only one column.
        Ignore the first row (header).
        positive_prompt are strings separated by comma. Each string is a prompt.
        negative_prompt are strings separated by comma. Each string is a prompt.

        Returns:
            list: List of artmovements. Each style is a dict with keys: style_name and value: [positive_prompt, negative_prompt]
        """
        artmovements = {"Error loading artmovements.csv, check the console": ["",""]}
        if not os.path.exists(artmovements_path):
            print(f"""Error. No artmovements.csv found. Put your artmovements.csv in the root directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """)
            return artmovements
        try:
            with open(artmovements_path, "r", encoding="utf-8") as f:    
                artmovements = [[x.replace('"', '').replace('\n','') for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)] for line in f.readlines()[1:]]
                artmovements = {x[0]: [x[1],x[2]] for x in artmovements}
        except Exception as e:
            print(f"""Error loading artmovements.csv. Make sure it is in the root directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """)
        return artmovements
        
    @classmethod
    def INPUT_TYPES(cls):
        cls.artmovements_csv = cls.load_artmovements_csv(os.path.join(folder_paths.base_path, "custom_nodes\\ComfyUI-CSV_Loader\\CSV\\artmovements.csv"))
        return {
            "required": {
                "artmovements": (list(cls.artmovements_csv.keys()),),
            },
                                
        }

    RETURN_TYPES = ("STRING","STRING")
    RETURN_NAMES = ("positive prompt", "negative prompt")
    FUNCTION = "execute"
    CATEGORY = "CSV Loaders"   

    def execute(self, artmovements):
            return (self.artmovements_csv[artmovements][0], self.artmovements_csv[artmovements][1])


#CHARACTERS

class CharactersCSVLoader:
    """
    Loads csv file with characters. For migration purposes from automatic11111 webui.
    """
    
    @staticmethod
    def load_characters_csv(characters_path: str):
        """Loads csv file with characters. It has only one column.
        Ignore the first row (header).
        positive_prompt are strings separated by comma. Each string is a prompt.
        negative_prompt are strings separated by comma. Each string is a prompt.

        Returns:
            list: List of characters. Each style is a dict with keys: style_name and value: [positive_prompt, negative_prompt]
        """
        characters = {"Error loading characters.csv, check the console": ["",""]}
        if not os.path.exists(characters_path):
            print(f"""Error. No characters.csv found. Put your characters.csv in the root directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """)
            return characters
        try:
            with open(characters_path, "r", encoding="utf-8") as f:    
                characters = [[x.replace('"', '').replace('\n','') for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)] for line in f.readlines()[1:]]
                characters = {x[0]: [x[1],x[2]] for x in characters}
        except Exception as e:
            print(f"""Error loading characters.csv. Make sure it is in the root directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """)
        return characters
        
    @classmethod
    def INPUT_TYPES(cls):
        cls.characters_csv = cls.load_characters_csv(os.path.join(folder_paths.base_path, "custom_nodes\\ComfyUI-CSV_Loader\\CSV\\characters.csv"))
        return {
            "required": {
                "characters": (list(cls.characters_csv.keys()),),
            },
                                
        }

    RETURN_TYPES = ("STRING","STRING")
    RETURN_NAMES = ("positive prompt", "negative prompt")
    FUNCTION = "execute"
    CATEGORY = "CSV Loaders"   

    def execute(self, characters):
            return (self.characters_csv[characters][0], self.characters_csv[characters][1])


# COMPOSITION

class CompositionCSVLoader:
    """
    Loads csv file with composition. For migration purposes from automatic11111 webui.
    """
    
    @staticmethod
    def load_composition_csv(composition_path: str):
        """Loads csv file with composition. It has only one column.
        Ignore the first row (header).
        positive_prompt are strings separated by comma. Each string is a prompt.
        negative_prompt are strings separated by comma. Each string is a prompt.

        Returns:
            list: List of composition. Each style is a dict with keys: style_name and value: [positive_prompt, negative_prompt]
        """
        composition = {"Error loading composition.csv, check the console": ["",""]}
        if not os.path.exists(composition_path):
            print(f"""Error. No composition.csv found. Put your composition.csv in the root directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """)
            return composition
        try:
            with open(composition_path, "r", encoding="utf-8") as f:    
                composition = [[x.replace('"', '').replace('\n','') for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)] for line in f.readlines()[1:]]
                composition = {x[0]: [x[1],x[2]] for x in composition}
        except Exception as e:
            print(f"""Error loading composition.csv. Make sure it is in the root directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """)
        return composition
        
    @classmethod
    def INPUT_TYPES(cls):
        cls.composition_csv = cls.load_composition_csv(os.path.join(folder_paths.base_path, "custom_nodes\\ComfyUI-CSV_Loader\\CSV\\composition.csv"))
        return {
            "required": {
                "composition": (list(cls.composition_csv.keys()),),
            },
                                
        }
    
    RETURN_TYPES = ("STRING","STRING")
    RETURN_NAMES = ("positive prompt", "negative prompt")
    FUNCTION = "execute"
    CATEGORY = "CSV Loaders"   

    def execute(self, composition):
            return (self.composition_csv[composition][0], self.composition_csv[composition][1])


#LIGHTING
class LightingCSVLoader:
    """
    Loads csv file with lighting. For migration purposes from automatic11111 webui.
    """
    
    @staticmethod
    def load_lighting_csv(lighting_path: str):
        """Loads csv file with lighting. It has only one column.
        Ignore the first row (header).
        positive_prompt are strings separated by comma. Each string is a prompt.
        negative_prompt are strings separated by comma. Each string is a prompt.

        Returns:
            list: List of lighting. Each style is a dict with keys: style_name and value: [positive_prompt, negative_prompt]
        """
        lighting = {"Error loading lighting.csv, check the console": ["",""]}
        if not os.path.exists(lighting_path):
            print(f"""Error. No lighting.csv found. Put your lighting.csv in the root directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """)
            return lighting
        try:
            with open(lighting_path, "r", encoding="utf-8") as f:    
                lighting = [[x.replace('"', '').replace('\n','') for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)] for line in f.readlines()[1:]]
                lighting = {x[0]: [x[1],x[2]] for x in lighting}
        except Exception as e:
            print(f"""Error loading lighting.csv. Make sure it is in the root directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """)
        return lighting
        
    @classmethod
    def INPUT_TYPES(cls):
        cls.lighting_csv = cls.load_lighting_csv(os.path.join(folder_paths.base_path, "custom_nodes\\ComfyUI-CSV_Loader\\CSV\\lighting.csv"))
        return {
            "required": {
                "lighting": (list(cls.lighting_csv.keys()),),
            },
                                
        }
    
    RETURN_TYPES = ("STRING","STRING")
    RETURN_NAMES = ("positive prompt", "negative prompt")
    FUNCTION = "execute"
    CATEGORY = "CSV Loaders"

    def execute(self, lighting):
            return (self.lighting_csv[lighting][0], self.lighting_csv[lighting][1])


#SETTING

class SettingsCSVLoader:
    """
    Loads csv file with settings. For migration purposes from automatic11111 webui.
    """
    
    @staticmethod
    def load_settings_csv(settings_path: str):
        """Loads csv file with settings. It has only one column.
        Ignore the first row (header).
        positive_prompt are strings separated by comma. Each string is a prompt.
        negative_prompt are strings separated by comma. Each string is a prompt.

        Returns:
            list: List of settings. Each style is a dict with keys: style_name and value: [positive_prompt, negative_prompt]
        """
        settings = {"Error loading settings.csv, check the console": ["",""]}
        if not os.path.exists(settings_path):
            print(f"""Error. No settings.csv found. Put your settings.csv in the root directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """)
            return settings
        try:
            with open(settings_path, "r", encoding="utf-8") as f:    
                settings = [[x.replace('"', '').replace('\n','') for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)] for line in f.readlines()[1:]]
                settings = {x[0]: [x[1],x[2]] for x in settings}
        except Exception as e:
            print(f"""Error loading settings.csv. Make sure it is in the root directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """)
        return settings
        
    @classmethod
    def INPUT_TYPES(cls):
        cls.settings_csv = cls.load_settings_csv(os.path.join(folder_paths.base_path, "custom_nodes\\ComfyUI-CSV_Loader\\CSV\\settings.csv"))
        return {
            "required": {
                "settings": (list(cls.settings_csv.keys()),),
            },
                                
        }
    
    RETURN_TYPES = ("STRING","STRING")
    RETURN_NAMES = ("positive prompt", "negative prompt")
    FUNCTION = "execute"
    CATEGORY = "CSV Loaders"

    def execute(self, settings):
            return (self.settings_csv[settings][0], self.settings_csv[settings][1])


#STYLE

class StylesCSVLoader:
    """
    Loads csv file with styles. For migration purposes from automatic11111 webui.
    """
    
    @staticmethod
    def load_styles_csv(styles_path: str):
        """Loads csv file with styles. It has only one column.
        Ignore the first row (header).
        positive_prompt are strings separated by comma. Each string is a prompt.
        negative_prompt are strings separated by comma. Each string is a prompt.

        Returns:
            list: List of styles. Each style is a dict with keys: style_name and value: [positive_prompt, negative_prompt]
        """
        styles = {"Error loading styles.csv, check the console": ["",""]}
        if not os.path.exists(styles_path):
            print(f"""Error. No styles.csv found. Put your styles.csv in the root directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """)
            return styles
        try:
            with open(styles_path, "r", encoding="utf-8") as f:    
                styles = [[x.replace('"', '').replace('\n','') for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)] for line in f.readlines()[1:]]
                styles = {x[0]: [x[1],x[2]] for x in styles}
        except Exception as e:
            print(f"""Error loading styles.csv. Make sure it is in the root directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """)
        return styles
        
    @classmethod
    def INPUT_TYPES(cls):
        cls.styles_csv = cls.load_styles_csv(os.path.join(folder_paths.base_path, "custom_nodes\\ComfyUI-CSV_Loader\\CSV\\styles.csv"))
        return {
            "required": {
                "styles": (list(cls.styles_csv.keys()),),
            },
                                
        }

    RETURN_TYPES = ("STRING","STRING")
    RETURN_NAMES = ("positive prompt", "negative prompt")
    FUNCTION = "execute"
    CATEGORY = "CSV Loaders"   

    def execute(self, styles):
            return (self.styles_csv[styles][0], self.styles_csv[styles][1])


#POSITIVE

class PositiveCSVLoader:
    """
    Loads csv file with positive. For migration purposes from automatic11111 webui.
    """
    
    @staticmethod
    def load_positive_csv(positive_path: str):
        """Loads csv file with positive. It has only one column.
        Ignore the first row (header).
        positive_prompt are strings separated by comma. Each string is a prompt.
        negative_prompt are strings separated by comma. Each string is a prompt.

        Returns:
            list: List of positive. Each style is a dict with keys: style_name and value: [positive_prompt, negative_prompt]
        """
        positive = {"Error loading positive.csv, check the console": ["",""]}
        if not os.path.exists(positive_path):
            print(f"""Error. No positive.csv found. Put your positive.csv in the root directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """)
            return positive
        try:
            with open(positive_path, "r", encoding="utf-8") as f:    
                positive = [[x.replace('"', '').replace('\n','') for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)] for line in f.readlines()[1:]]
                positive = {x[0]: [x[1],x[2]] for x in positive}
        except Exception as e:
            print(f"""Error loading positive.csv. Make sure it is in the root directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """)
        return positive
        
    @classmethod
    def INPUT_TYPES(cls):
        cls.positive_csv = cls.load_positive_csv(os.path.join(folder_paths.base_path, "custom_nodes\\ComfyUI-CSV_Loader\\CSV\\positive.csv"))
        return {
            "required": {
                "positive": (list(cls.positive_csv.keys()),),
            },
                                
        }

    RETURN_TYPES = ("STRING","STRING")
    RETURN_NAMES = ("positive prompt", "negative prompt")
    FUNCTION = "execute"
    CATEGORY = "CSV Loaders"   

    def execute(self, positive):
            return (self.positive_csv[positive][0], self.positive_csv[positive][1])


#NEGATIVE

class NegativeCSVLoader:
    """
    Loads csv file with negative. For migration purposes from automatic11111 webui.
    """
    
    @staticmethod
    def load_negative_csv(negative_path: str):
        """Loads csv file with negative. It has only one column.
        Ignore the first row (header).
        positive_prompt are strings separated by comma. Each string is a prompt.
        negative_prompt are strings separated by comma. Each string is a prompt.

        Returns:
            list: List of negative. Each style is a dict with keys: style_name and value: [positive_prompt, negative_prompt]
        """
        negative = {"Error loading negative.csv, check the console": ["",""]}
        if not os.path.exists(negative_path):
            print(f"""Error. No negative.csv found. Put your negative.csv in the root directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """)
            return negative
        try:
            with open(negative_path, "r", encoding="utf-8") as f:    
                negative = [[x.replace('"', '').replace('\n','') for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)] for line in f.readlines()[1:]]
                negative = {x[0]: [x[1],x[2]] for x in negative}
        except Exception as e:
            print(f"""Error loading negative.csv. Make sure it is in the root directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """)
        return negative
        
    @classmethod
    def INPUT_TYPES(cls):
        cls.negative_csv = cls.load_negative_csv(os.path.join(folder_paths.base_path, "custom_nodes\\ComfyUI-CSV_Loader\\CSV\\negative.csv"))
        return {
            "required": {
                "negative": (list(cls.negative_csv.keys()),),
            },
                                
        }

    RETURN_TYPES = ("STRING","STRING")
    RETURN_NAMES = ("positive prompt", "negative prompt")
    FUNCTION = "execute"
    CATEGORY = "CSV Loaders"   

    def execute(self, negative):
            return (self.negative_csv[negative][0], self.negative_csv[negative][1])


#NODE NAMING

NODE_CLASS_MAPPINGS = {
    "Load Artists CSV": ArtistsCSVLoader,
    "Load Artmovements CSV": ArtmovementsCSVLoader,
    "Load Characters CSV": CharactersCSVLoader,
    "Load Composition CSV": CompositionCSVLoader,
    "Load Lighting CSV": LightingCSVLoader,
    "Load Settings CSV": SettingsCSVLoader,
    "Load Styles CSV": StylesCSVLoader,
    "Load Positive CSV": PositiveCSVLoader,
    "Load Negative CSV": NegativeCSVLoader

}
NODE_DISPLAY_NAME_MAPPINGS = {
    "ArtistsCSVLoader": "Load Artists CSV Node",
    "ArtmovementsCSVLoader": "Load Art Movements CSV Node",
    "CharactersCSVLoader": "Load Characters CSV Node",
    "CompositionCSVLoader": "Load Composition CSV Node",
    "LightingCSVLoader": "Load Lighting CSV Node",
    "SettingsCSVLoader": "Load Settings CSV Node",
    "StylesCSVLoader": "Load Styles CSV Node",
    "PositiveCSVLoader": "Load Positive CSV Node",
    "NegativeCSVLoader": "Load Negative CSV Node"
    
}