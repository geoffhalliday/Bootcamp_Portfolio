:: If the folder 'new_folder' exists a new folder called 'if_folder' is created
if exist new_folder mkdir if_folder
:: If the folder 'if_folder' exists, a new folder called 'hyperionDev' is created; else a new folder called 'new-projects' is created
if exist if_folder (mkdir hyperionDev) else (mkdir new-projects)