# How to use Git and GitHub.
[Command sheet ref.](https://qiita.com/okamu_/items/d52a6900311ad9073628)
## Create local repository.
At your working directory.
```
$ git init
```

## Add and Commit
If you alresdy have some files what you want to upload, let's do add and commit to local repository.
```
$ git add <file-name>
$ git commit -m "<prefix>: <some comments>"
```
Please refer to DEVELOPERS.md about prefix.

## Push to remote repository
### First time to push
```
$ git remote add origin <remote repository URL>
$ git push origin master
```
### Not first time
```
$ git push origin master
```
### If you rejected git push
It offten occurs at first time push.
Remote repository and local repository had different information at first.<br>
Then, need to merge at first.
```
$ git merge --allow-unrelated-histories origin/master
```
Ex.
```
PS D:\Dropbox\03_総研大\ATF\ATF2-magnet-mover> git pull origin master
From https://github.com/YUKI-SOKENDAI/MagnetMoverFB                                                                      
* branch            master     -> FETCH_HEAD                                                                           
fatal: refusing to merge unrelated histories

PS D:\Dropbox\03_総研大\ATF\ATF2-magnet-mover> git push origin master                                                   
To https://github.com/YUKI-SOKENDAI/MagnetMoverFB.git                                                                    
! [rejected]        master -> master (non-fast-forward)                                                                
error: failed to push some refs to 'https://github.com/YUKI-SOKENDAI/MagnetMoverFB.git'                                 
hint: Updates were rejected because the tip of your current branch is behind                                            
hint: its remote counterpart. Integrate the remote changes (e.g.                                                        
hint: 'git pull ...') before pushing again.                                                                             
hint: See the 'Note about fast-forwards' in 'git push --help' for details.  
```

### Not recommended technic
When we push to remote repository, we got some issues sometimes.
Then, we can't push well to remote repository.
There is technic to force pushing to remote repository.
```
$ git push -f origin master
```
* It works anytime. But update all forcibly. Need to pay attention. Especially, you work with other coraborators.

## Make branch
```
$ git checkout -b <branch-name>
```
## Pull and Merge
```
$ git pull origin master
$ git pull origin <branch-name>
```
