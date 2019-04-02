;等待Title为phpwind - Powered by phpwind - Google Chrome的窗口
Local $win = WinWaitActive("phpwind - Powered by phpwind - Google Chrome","",10)

;在本机分辨率宽度为1616，高度为876的情况下，对坐标点（630，507）进行鼠标左击
$pos =WinGetPos($win)
$high=$pos[3];表示窗口的的实际高度
$weight=$pos[2];表示窗口的实际宽度
$click_x=630*$weight/1616;630表示我在当前电脑分辨率宽度为1616下的X坐标值
$click_y=507*$high/876;507表示我再当前电脑分辨率高度为876下的Y坐标值
MouseClick("left",$click_x,$click_y,1)

;等待Class为#32770的窗体
WinWaitActive("[CLASS:#32770]","",10)
;把焦点设置在controllID为Edit1的控件中
ControlFocus("打开","","Edit1")
;设置该控件的文本为C:\Users\qvzn0\Pictures\test.jpeg
ControlSetText("打开","","Edit1","C:\Users\qvzn0\Pictures\test.jpeg")
;点击controllID为Button1的控件
ControlClick("打开","","Button1")
Sleep(2000)

;提交flash
$click_x2=535*$weight/1616
$click_y2=715*$high/876
MouseClick("left",$click_x2,$click_y2,1)
Sleep(2000)