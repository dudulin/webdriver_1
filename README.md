### 监听用户操作

pip install pynput
目前支持鼠标和键盘的控制与监听


    a = pyautogui.confirm('选择一项', buttons=['A', 'B', 'C'])
    if a == 'A':
        driver.close()
        driver.quit()

使用 pyautogui.confirm  来关闭浏览器

---