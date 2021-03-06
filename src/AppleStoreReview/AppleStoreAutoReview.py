#coding=utf-8
##############################################
#
# Author:       Shen Wenrui
# Date:         20180407
# Description:
#
##############################################

import applescript

scpt = applescript.AppleScript('''
    -- Function for iTunes sign in
    property storeNmae : "Store"        --"商店"
    property loginBtn : "Sign In…"      --"登录…"
    property logoutBtn : "Sign Out"     --"注销"
    -- Launch iTunes
    
    on openAppStore (appleId, passwd)
        tell application "App Store" to activate
        tell application "System Events"
            tell process "App Store"
                set frontmost to true
                delay 10
                try
                    click menu item 12 of menu 1 of menu bar item 4 of menu bar 1 -- "Sign In…"
                on error
                    click menu item 12 of menu 1 of menu bar item 4 of menu bar 1 -- "Sign Out"
                    delay 2
                    click menu item 12 of menu 1 of menu bar item 4 of menu bar 1 -- "Sign In…"
                end try
                
                delay 10
                set value of text field 2 of sheet 1 of window "App Store" to appleId
                set value of text field 1 of sheet 1 of window "App Store" to passwd
                
                -- Press the return key "登陆"
                click button 3 of sheet 1 of window "App Store" 
                --keystroke return 
                
                delay 15
                -- Click Review
                click button 1 of sheet 1 of window "App Store"
                --keystroke return
                
                delay 15
                --select the aggrement of the condition.
                click checkbox 1 of group 5 of UI element 1 of scroll area 1 of group 1 of group 1 of window "App Store"
                --press continue
                click button 2 of group 6 of UI element 1 of scroll area 1 of group 1 of group 1 of window "App Store"
                
                delay 8
                --select 'Mr.'
                click pop up button 1 of group 3 of UI element 1 of scroll area 1 of group 1 of group 1 of window "App Store"
                click menu item 2 of menu 1 of group 1 of window "App Store"
                --press continue
                click button 3 of group 7 of UI element 1 of scroll area 1 of group 1 of group 1 of window "App Store"
                
                delay 10
                --select 'None' as the payment method
                click radio button 6 of group 6 of UI element 1 of scroll area 1 of group 1 of group 1 of window "App Store"
                --press continue
                (*delay 1
                click button 3 of group 14 of UI element 1 of scroll area 1 of group 1 of group 1 of window "App Store"
                
                delay 10
                --Welcom page -> Continue
                click button 1 of sheet 1 of window "App Store"*)
                
            end tell
        end tell
        
        return True
    end openAppStore
''')

#user_email = "zhangtao001@protonmail.com"
#user_password = "Apple_swr123"

#user_email = "guanjinxi001a@protonmail.com"
#user_password = "Apple_gjx123"

user_email = "shijiachen001a@protonmail.com"
user_password = "Apple_sjc123"

print(scpt.call('openAppStore', user_email, user_password))