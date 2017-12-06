# FlaskDemo
Using Flask to build web

資料夾結構：
1. 沒有使用Package（Teacher's case)
   /FlaskDemo
      /templates (html或其他種類的頁面檔案，此為render_template預設尋找檔案的路徑)
        index.html
      /static (可以把CSS, Javascript放在這個資料夾)
      /env (虛擬環境)
      Hello_Flask.py
      
2. 有使用Package
  /FlaskDemo
      /Package
          /__init__.py  （這個檔案一定要有，應是Python用來識別此區塊內的檔案都屬於此Package，裡面的程式碼空白沒關係）
          /templates (html或其他種類的頁面檔案，此為render_template預設尋找檔案的路徑)
              /index.html
          /static (可以把CSS, Javascript放在這個資料夾)
          /Hello_Flask.py
      /env (虛擬環境)
      
P.S.此範例資料夾結構為第一種

執行步驟：
1. 由於目前flask只有安裝在虛擬環境，所以要進入到正確的虛擬環境內，以此專案為例，必須進入../FlaskDemo/env/bin/ 執行 activate (windows和mac啟用指令不同)
2. 確認進入虛擬環境後執行撰寫好的主程式。 Windows : python Hello_Flask.py   Mac: python3 Hello_Flask.py （示意執行方式，要注意指到對的路徑)
3. 若執行成功的話，Console會顯示如下訊息：（表示已經於本機成功啟用)
 * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 280-562-887
4. 驗證執行結果，於瀏覽器輸入http://127.0.0.1:8080/hello (此範例為此路徑，個人可自行設定，詳情見Hello_Flask.py)


