#!/bin/bash
for direc in spotipy tinydb dynaconf gspread oauth2client
do

   for eachfile in `ls playlist/vendor_src/$direc/*.py`
   do
      pyminify --remove-literal-statements $eachfile > ${eachfile/_src/''}
   done

done
