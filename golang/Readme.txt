Rama para desarrollos Golang
Se trabaja desde ATOM y se PUSH a GitHub para
luego desde "malla" hacerlo pull en la rama de "desarrollo"
de "malla":

oficina@malla:/var/www/vue.js$ git branch -a
* desarrollo
  master
  remotes/origin/HEAD -> origin/master
  remotes/origin/cursos
  remotes/origin/desarrollo
  remotes/origin/golang
  remotes/origin/master
oficina@malla:/var/www/vue.js$ git pull origin golang
From https://github.com/LeasenCloud/vue.js
 * branch            golang     -> FETCH_HEAD
   c7a8c2d..bb0b496  golang     -> origin/golang
Already up-to-date.
<<<<<<< HEAD
=======

>>>>>>> 427f77ba41660cc9da18c2867af9596144042fc0
