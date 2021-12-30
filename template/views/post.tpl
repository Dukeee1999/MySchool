<!doctype html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">

<link rel="stylesheet" type="text/css" href="../layui/css/layui.css" media="all">
<style type="text/css">
.article-container{
    background-color: #ffffff;
    padding-top:20px;
    width:1024px;
    margin:20px auto;
  }

  .article_r{
    padding-top:10px;
    float:right;
  }
  .pulisher,.time,.article_view,.article_comments,.article_del{
    clear:both;
    margin-right:25px;
    font-size: 15px;
  }
  .title{
    font-weight:bold;
    font-size: 30px;
    text-align: center;
  }
  .article_content{
    background: #ffffff;
    clear:both;
    padding:1em 4em;
    margin-top: 40px;
  }
  p{
    text-indent: 2em;
    text-overflow: hidden;
    font-size:18px;
  }

  /*IMG*/
  .ImgContent{
    width:350px;
    margin:0px auto;
    padding: 5px;
    overflow:hidden;

}

.NavLinks{
    padding:5px;
    width:100px;
    height: 100px;
    float: left;
    overflow: hidden;
}

.NavLinks img{
    width: 100%;
    height: 100%;
}
.hitShowPic {
width:350px;
clear:both;
margin-left:430px;
}
.hitShowPic span {
  font-size: 15px;
  text-align: center;
}
   .show_reply_list {
    margin-right:1em;
     color: grey;
   }
    .comment_list {
    background-color: #ffffff;
    padding-top:5px;
    width:900px;
    margin:0 auto;
  }
    .comment {
      width:900px;
      margin-top:10px;
    }
    .comment_details {
      float:right;
    }
    .comment_content {
      clear:both;
      margin:5px 50px;
      font-size:16px;
    }
  .comment_add_or_last {

    margin:0 auto;
    clear: both;
    width:600px;
    height:50px;
    background: #F0F0F0;
    text-align: center;
    font-size:20px;
     line-height: 40px;
     margin-bottom: 40px;
  }
  .imgdiv{
       width:80px;
       height:70px;
      float:left;

  }
  .imgcss {
    width:60px;
    height:60px;
    border-radius: 50%;
  }
  .comment_name {
    margin-left:10px;
    color:#3D9EEA;
    font-size:16px;
    font-weight: bolder;
  }
  .layui-icon {
    font-size: 13px;
    color: grey;
  }
  .del {
    float:right;

  }
  .del_comment {
     margin-right:50px;
  }



  .reply_list {
    clear:both;
    display:none;
    width:900px;

    padding-right:15px;
    margin-top:10px;
      font-size:16px;

  }
  .reply {
    clear:both;
    width:700px;
    margin:4px auto;

  }
  .reply_name {
    color:#3D9EEA;
  }
  .del_reply {
      float:right;
  }
  .show_remain_reply {
     width:600px;
     height:40px;
     text-align:center;font-size:18px;
     background-color: #F0F0F0;
     margin:0 auto;
     line-height: 40px;
     display:none;
  }
</style>
<link rel="stylesheet" href="../../layui/css/layui.css">
<!--?  <link rel="stylesheet" href="css/global.css">-->
    <style>
        html{overflow-x: hidden; overflow-y: auto; background-color: #eee; }
        body{line-height:24px;}
        i{font-style: normal;}
        .main{width: 800px; min-height: 600px; margin: 0 auto 15px;}
        body input, body textarea{box-shadow:none;}
        body .layui-layer-prompt textarea.layui-layer-input{resize: both;}
    </style>
<script src="../../layui/layui.js"></script>
</head>
<body>
 % include('/home/yunqi/git_version/INFO2222-Group-Project/template/views/header.tpl')
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="../../css/index.css">

<div class="article-container">

        <div class="article_head">
            <h1 class="title">{{post["title"]}}</h1>
            <div class="article_r">
             <span class="pulisher">{{post["username"]}}  Posted at</span>
            <span class="time">  {{post["post_time"]}}</span>
            % if comments !=None:
                <span class="article_comments" title="comment: "> <a href="#" onclick=""> Comment Number: </a> {{len(comments)}}</span>
            % end
            % if comments ==None:
                <span class="article_comments" title="comment: "> <a href="#" onclick=""> Comment Number: </a> 0 </span>
            % end
            % if username == 'admin':
                <span class="article_del" data-id="${articleDto.id}"><a href="/post/{{post["post_id"]}}" onclick="" title="delete">Delete</a></span>
               %end
            </div>
        </div>
        <div class="article_content">
             <p> {{post["content"]}}</p>
        </div>
        <hr/>

      %if comments != None:
      <div class="comment_list">
        <h3 style="text-indent: 2em;">Comments</h3>
        %for comment in comments:
        <hr>
            <div class="comment">
               <div class="conmment_details">
                  <div style="float:left;">
                    <span class="comment_name">{{comment["username"]}}</span>     <span>{{comment["post_time"]}}</span>

                  </div>
                  % if username == 'admin':
                  <div class="del">
                    <a class="del_comment" data-id="1" href='/comment/{{post["post_id"]}}/{{comment["Id"]}}' > <i class="icon layui-icon" >Delete</i></a>
                  </div>
                  % end
                   <div class="comment_content" >
                     <p>
                       {{comment["content"]}}
                     </p>
                  </div>
              </div>
          </hr>
          %end
      </div>
      %end

<hr>
<div class="main layui-clear">
  <div class="fly-panel" pad20>
    % if mute =='0':
    <h2 class="page-title">Post your comment!</h2>

    <div class="layui-form layui-form-pane">
      <form action="/new-comment/{{post['post_id']}}" method="post">
        <input type="hidden" id="usrname" name="usrname" value>
        <div class="layui-form-item">
        </div>
        <div class="layui-form-item layui-form-text">
          <div class="layui-input-block">
             <div class="editor">
    			<textarea id="content" name="content" style="width:800px;height:200px;visibility:hidden;"></textarea>
  			 </div>
          </div>
        </div>
        <div class="layui-form-item">
          <button class="layui-btn" lay-filter="*" lay-submit>Post now!</button>
        </div>
      </form>
    </div>
    % end
  </div>
</div>
</hr>
 <script type="text/javascript" charset="utf-8" src="../../js/kindeditor.js"></script>
  <script type="text/javascript">
    KE.show({
        id : 'content',
		resizeMode : 1,
        cssPath : './index.css',
        items : [
        'fontname', 'fontsize', 'textcolor', 'bgcolor', 'bold', 'italic', 'underline',
        'removeformat', 'justifyleft', 'justifycenter', 'justifyright', 'insertorderedlist',
        'insertunorderedlist', 'emoticons', 'image', 'link']
    });
    if(getCookie('username')) {
      var a = document.getElementById('usrname');
      var b = getCookie('username')
      console.log(getCookie('username'))
      a.setAttribute("value",b)
            }
  </script>


</body>
</html>
