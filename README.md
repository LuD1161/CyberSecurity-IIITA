# CyberSecurity-IIITA
A Repo to keep the CyberSecurity-IIITA projects 

## How to get started 

Steps : 

- Create a fork of the project
- Clone the fork on your system ( using `git clone <link to the repo>` )
- On your fork , first check which branch you're on ( make sure you're on the branch everyone's working on , in this case **master branch** ) , using the command `git branch`
- Then create a branch from that branch ( development ) , using `git checkout -b <branch_name>`.
e.g. - If you're working on notifications , make a branch named suppose **notification-issue**
Then you would be doing it like this : 
`git checkout -b notification-issue`
- After you've done some work and wish to save it then commit those files , I prefer `pycharm` , it has a good versioning system.
- Before pushing a repo you need to define where the repo is to be pushed, it's called remote-url , for more details check [here](https://help.github.com/articles/adding-a-remote/). 
Check the output of this command `git remote -v`
If you have downloaded it from your fork , you would get something like this 
```
origin  https://github.com/user/<your-repo>.git (fetch)
origin  https://github.com/user/<your-repo>.git (push)
```
You will always be pushing to your own repo ( cause you don't have write access to my repo ) and then make a **new PR** for the same.

When an issues is complete , go to the terminal and from the repo's root directory make a push statement , like this : 

`git push -f origin <the_branch_name>` 
e.g. -  `git push -f origin notification-issue` 

A new branch would be created on your repo ( if it didn't already existed ) or it will be updated ( if it already existed )

Then make a new PR for the same.

Below is the screenshot for the whole process : 
![image](https://user-images.githubusercontent.com/17861054/27622278-baf3305c-5bf3-11e7-9c34-e6c1786a3ac7.png)

The last command is just to delete the branch remotely i.e. on my git repo ( instead of locally ).

**The video depicting the whole process is [here](https://www.youtube.com/watch?v=4_-E5l15gDU). **
