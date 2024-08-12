#!/bin/bash

oldfile="Es9ZY.tar.xz"
defaultcontent="Is_this_password?"
content=""
tar xf $oldfile  #unzipping the Es9ZY.tar.xz
                 #I dont want to delete the original file so i keep it outside the loop

while true; do    #Using while loop because the number of tar.xz file is unknown
    listfilename=$(ls)     #In a loop, I will check every files in directory
    checktar=false         #set a boolean value to check if there is .tar.xz file or not 
    for eachfile in $listfilename   #loop through every file in current directory
    do
        #check the content of the same.txt, if the content is diffirence, it might be the password for the 0.zip
        #then save the diffirence content to the password.txt
        if [[ "$eachfile" == "same.txt" ]]; then
            content=$(cat $eachfile)
            if [[ $content != $defaultcontent ]]; then
                echo "$content" > password.txt
            fi
        #unzip the .tar.xz and remove the old one
        elif [[ $eachfile == *.tar.xz ]] && [[ $eachfile != $oldfile ]]; then
            tar xf $eachfile
            rm $eachfile
            checktar=true
        fi
    done
    if [[ "$checktar" == "false" ]]; then
        break
    fi
done
