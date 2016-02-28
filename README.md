##Rails Part
after installing rails, the way to create a rails app with a 
a good guide for rails is
http://guides.rubyonrails.org/getting_started.html

###in the command line:

$ ruby -v
ruby 2.0.0p353

$ gem install rails
rails new my_great_app -T -d postgresql --skip-turbolinks

After it's done installing it you need to bundle
(make sure you are inside the right file)
$ bundle

####to access the server:
$ rails s
in the browser : http://localhost:3000/
you kill a server with control + c
you kill a rouge server with  $ ps aux | grep shotgun  or $ lsof -i TCP:9393

####to access the console:
$rails c

