from stock_fish import ChessCLI
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


def start_browser():
    browser = webdriver.Chrome()
    browser.get('https://chess.com/')

    start_game = browser.find_element(By.CSS_SELECTOR, 'body > div.base-layout > div.base-container > main > div > div > section.index-guest-block > div.index-intro > div.index-guest-button-wrap > form > button')
    start_game.click()

    st_game = browser.find_element(By.CSS_SELECTOR, 'body > div.cc-modal-component > div.cc-modal-body.cc-modal-md > button')
    st_game.click()

    game_mode_selector = browser.find_element(By.CSS_SELECTOR, '#board-layout-sidebar > div.sidebar-component > div.new-game-index-component > div.new-game-index-content > div > div:nth-child(1) > button')
    game_mode_selector.click()

    game_mode = browser.find_element(
        By.CSS_SELECTOR,
        '#board-layout-sidebar > div.sidebar-component > div.new-game-index-component > div.new-game-index-content > div > div:nth-child(1) > div > div:nth-child(2) > div.time-selector-field-component > button:nth-child(3)'
    )
    game_mode.click()
    game_starter = browser.find_element(By.CSS_SELECTOR, '#board-layout-sidebar > div.sidebar-component > div.new-game-index-component > div.new-game-index-content > div > button')
    game_starter.click()

    sleep(1000)


if __name__ == "__main__":
    # start_browser()

    game = ChessCLI()
    game.run()



