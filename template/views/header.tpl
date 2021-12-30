<head>
<link rel="stylesheet" type="text/css" href="css/temp.css">
<style>
    #login{
        float: right;
    }
    div{
        margin: auto;
        margin-bottom: 10px;
        margin-top: 13px;
    }
    #link2{
        color: whitesmoke;
        font-size: 16px;

    }
    .header{
        list-style-type: none;
        margin: 0;
        padding: 0;
        overflow: hidden;
        background-color: #333;
    }
    .header li {
        list-style-type: none;
        float: left;
    }

    .header li a{
            display: block;
            color: white;
            text-align: center;
            padding: 14px 16px;
            text-decoration: none;
        }

    .header li a:hover {
            background-color: #111;
    }
    .header li text{
        display: block;
        text-align: center;
        padding: 14px 100px;
        color: whitesmoke;
        text-decoration: none;
    }

</style>

<script type="text/javascript">
        function getCookie(cname) {
          var name = cname + "=";
          var decodedCookie = decodeURIComponent(document.cookie);
          var ca = decodedCookie.split(';');
          for(var i = 0; i <ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0) == ' ') {
              c = c.substring(1);
            }
            if (c.indexOf(name) == 0) {
              return c.substring(name.length, c.length);
            }
          }
          return "";
        }

        function setCookie(cname, cvalue, exdays) {
            var d = new Date();
            d.setTime(d.getTime() + (exdays*24*60*60*1000));
            var expires = "expires="+d.toUTCString();
            document.cookie = cname + "=" + cvalue + "; " + expires;
        }

        function clearCookie(name) {
            setCookie(name, "", -1);
        }

</script>
</head>

<ul class="header">
  <li><a class="active" href="/home">Home</a></li>
  <li><a href="/html-home">Learn HTML</a></li>
  <li><a href="/css-home">Learn CSS</a></li>
  <li><a href="/express-intro">Learn Express</a></li>
  <li><a href="/JavaScript">Learn JavaScript</a></li>
    <li><a id="forum" href="/forum">Forum</a></li>
  <li><a href="/about">About</a></li>
    <li><a id="background" style="display: none;" ></a></li>
    <script type='text/javascript'>
        if (getCookie('username') == 'admin') {
            var d = document.getElementById('background');
            d.setAttribute("href", '/manager')
            d.setAttribute("style", "display: block;")
            d.innerHTML = "manager";
        }
    </script>
  <li id = "login"><a id="link" href="/login"></a></li>
    <div id ="signout"><a id = "link2" href="/home"></a></div>
    <script type="text/javascript" src="js/jquery-1.7.2.js"></script>
    <script type="text/javascript">
        if(getCookie('username')) {
            var a = document.getElementById('link');
            var b = document.createElement('text');
            var c = document.getElementById('link2');
            b.innerHTML = "Welcome " + getCookie('username') + " !";
            a.parentElement.replaceChild(b,a);
            c.innerHTML = "SignOut"
        }else {
            document.getElementById('link').textContent = "Login";
        }
        $(function(){
            $("#signout").click(function (){
                clearCookie("username");
                clearCookie("user_id");
            })
        })

    </script>
</ul>
