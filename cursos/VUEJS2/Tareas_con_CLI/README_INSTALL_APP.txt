:~/Documentos/0Programar/tmp$ vue init webpack-simple myapp
        Command vue init requires a global addon to be installed.
        Please run npm install -g @vue/cli-init and try again.


:~/Documentos/0Programar/tmp$ cd ../node-v10.16.3-linux-x64/lib/node_modules


:~/Documentos/0Programar/node-v10.16.3-linux-x64/lib/node_modules$ npm install -g @vue/cli-init
        npm WARN deprecated vue-cli@2.9.6: This package has been deprecated in favour of @vue/cli
        npm WARN deprecated coffee-script@1.12.7: CoffeeScript on NPM has moved to "coffeescript" (no hyphen)
        + @vue/cli-init@3.11.0
        added 256 packages from 208 contributors in 21.843s


:~/Documentos/0Programar/node-v10.16.3-linux-x64/lib/node_modules$ cd -
        /home/u020531/Documentos/0Programar/tmp


:~/Documentos/0Programar/tmp$ vue init webpack-simple myapp
        ? Project name myapp
        ? Project description A Vue.js project
        ? Author gongolin <mdelrosal@leasencloud.com>
        ? License MIT
        ? Use sass? No

           vue-cli · Generated "myapp".

           To get started:

             cd myapp
             npm install
             npm run dev


:~/Documentos/0Programar/tmp$


:~/Documentos/0Programar/tmp/myapp$ npm install
          npm WARN deprecated flatten@1.0.2: I wrote this module a very long time ago; you should use something else.
          npm WARN deprecated browserslist@1.7.7: Browserslist 2 could fail on reading Browserslist >3.0 config used in other tools.

          > core-js@2.6.9 postinstall /home/u020531/Documentos/0Programar/tmp/myapp/node_modules/core-js
          > node scripts/postinstall || echo "ignore"

          Thank you for using core-js ( https://github.com/zloirock/core-js ) for polyfilling JavaScript standard library!

          The project needs your help! Please consider supporting of core-js on Open Collective or Patreon:
          > https://opencollective.com/core-js
          > https://www.patreon.com/zloirock

          Also, the author of core-js ( https://github.com/zloirock ) is looking for a good job -)

          > uglifyjs-webpack-plugin@0.4.6 postinstall /home/u020531/Documentos/0Programar/tmp/myapp/node_modules/uglifyjs-webpack-plugin
          > node lib/post_install.js

          npm notice created a lockfile as package-lock.json. You should commit this file.
          npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@1.2.9 (node_modules/fsevents):
          npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.2.9: wanted {"os":"darwin","arch":"any"} (current: {"os":"linux","arch":"x64"})

          added 786 packages from 569 contributors and audited 9895 packages in 72.533s
          found 8 vulnerabilities (4 moderate, 4 high)
            run `npm audit fix` to fix them, or `npm audit` for details


:~/Documentos/0Programar/tmp/myapp$


:~/Documentos/0Programar/tmp/myapp$ npm run dev
          > myapp@1.0.0 dev /home/u020531/Documentos/0Programar/tmp/myapp
          > cross-env NODE_ENV=development webpack-dev-server --open --hot

          Project is running at http://localhost:8080/
          webpack output is served from /dist/
          404s will fallback to /index.html
          { parser: "babylon" } is deprecated; we now treat it as { parser: "babel" }.
