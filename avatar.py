"""
Ref:
https://home.gamer.com.tw/creationDetail.php?sn=3669589
"""
import pygame
import time
import threading
from audio import TTS_google, TTS_py
from FixedBase import model_call

class Avatar:
    def __init__(self):
        pygame.init()

        # Set the window.
        self.window_size = (300, 510)
        self.window = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("CultechBot")

        # Load images.
        self.c_img = pygame.image.load("Avatar/closed_block.jpg")
        self.c_img = pygame.transform.scale(self.c_img, (300, 510))

        self.o_img = pygame.image.load("Avatar/opened_block.jpg")
        self.o_img = pygame.transform.scale(self.o_img, (300, 510))

        self.chinese_font = pygame.font.Font("Fonts/mingliu.ttc", 12)

        self.ans = None

        # Default image: closed mouth
        self.display_image(self.c_img)

    def display_image(self, image):
        self.window.blit(image, (0, 0))
        pygame.display.flip()

    # Simulate talking with voice.
    def simulation(self, text):
        text_render = self.chinese_font.render("小桂子: " + text, True, (0, 0, 0)) 
        loc = (10, 445)

        o_img = self.o_img.copy()
        o_img.blit(text_render, loc)
        c_img = self.c_img.copy()
        c_img.blit(text_render, loc)

        thread = threading.Thread(target=TTS_py, args=(text,))
        thread.start()
        
        while thread.is_alive():
            self.display_image(o_img)
            time.sleep(0.2)      # Show opened mouth image for 0.2 seconds.
            if thread.is_alive():
                self.display_image(c_img)
                time.sleep(0.2)  # Show closed mouth image for 0.2 seconds.
        self.display_image(c_img)
        
        thread.join()


    # llm_call, threaded
    def threaded_model_call(self, text):
        time.sleep(2)
        result = model_call(text)
        self.ans = result


    # Chatbot's thinking state.
    def thinking(self, text):
        text_render = self.chinese_font.render("你: " + text + "?", True, (0, 0, 0))  
        text_width, _ = text_render.get_size()
        text_x = (self.window_size[0] - 10 - text_width)
        loc = (text_x, 445)

        u_img = self.c_img.copy()
        u_img.blit(text_render, loc)

        thread = threading.Thread(target=self.threaded_model_call, args=(text,))
        thread.start()
        
        while thread.is_alive():
            self.display_image(u_img)
        
        thread.join()

        return self.ans
 

if __name__ == '__main__':
    avatar = Avatar() 

    text = "祝你天天開心!"
    avatar.simulation(text)