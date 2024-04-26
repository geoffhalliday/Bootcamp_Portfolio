:: I am creating 3 folders, named 'folder_1', 'folder_2' & 'folder_3'
mkdir folder_1
mkdir folder_2
mkdir folder_3
:: I then navigate inside folder_1 and create 3 new folders, named 'folder_a', 'folder_b' & 'folder_c'
cd folder_1
mkdir folder_a
mkdir folder_b
mkdir folder_c
:: I am instructed to remove 2 folders, but not told which, so have chosen to remove folder_2 and folder_3
cd ..\
rmdir folder_2
rmdir folder_3