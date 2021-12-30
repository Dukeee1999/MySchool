<!DOCTYPE html>
<html>

	<head>
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
						var b = document.createElement('text');
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
            </script>
</head>
<body>
% include('/home/yunqi/git_version/INFO2222-Group-Project/template/views/header.tpl')
<meta charset="utf-8" />
	<link rel="stylesheet" type="text/css" href="../css/index.css">
<div class="dvContent">
	<div class="dvquesleft">

		<div class="dvqstitle">
			<span class="qsTitle"></span>
		</div>
		<div class="dvtabhead">
			<div class="tabheads tabcurrent">All questions</div>
			<div class="tabheads">My question</div>
		</div>
		<div class="tabContent">
			<div class="tab">
            % if len(posts)!=0:
				% for post in posts:
					% if post['pinned']=="TRUE":
						%if user_id == '1':
						<a href="/unpin/{{post['post_id']}}">UNPIN</a>
						% end
					<div class="dvques">
						<div class="quesCount">
							<div class="count">{{my_dict[str(post['post_id'])]}}</div>
							<div class="ques">Number of answers</div>
						</div>

						<div class="quesContent">
							<div class="quesTitle"><div
									class="spanques"><a href="/forum/{{post['post_id']}}">{{post["title"]}}</a></div>
							</div>
							<div class="qContent">{{post["content"]}}</div>
							<div class="quesUser">
								</image src="img/avatar.gif" class="imguser" />
								<div class="userName">
									{{post['username']}}
								</div>
							</div>
						</div>
					</div>
					% end
				% end

				% for post in posts:
					% if post['pinned']=="FALSE":
					% if user_id == '1':
							<a href="/pin/{{post['post_id']}}">PIN</a>
					% end
					<div class="dvques">
						<div class="quesCount">
							<div class="count">{{my_dict[str(post['post_id'])]}}</div>
							<div class="ques">Number of answers</div>
						</div>

						<div class="quesContent">
							<div class="quesTitle"><div
									class="spanques"><a href="/forum/{{post['post_id']}}">{{post["title"]}}</a></div>
							</div>
							<div class="qContent">{{post["content"]}}</div>
							<div class="quesUser">
								</image src="img/avatar.gif" class="imguser" />
								<div class="userName">
									{{post['username']}}
								</div>
							</div>
						</div>
					</div>
					% end
				% end
			%end
			%if len(posts)==0:
			    <div class="error"> There is no post yet ! </div>
            %end
			</div>
			<div class="tab hidden">2</div>
			<div class="tab hidden">3</div>
			<div class="tab hidden">4</div>
		</div>
	</div>
	<div class="dvquesright">
	    % if mute=='0':
		<div>
			<buton id= "post_question" class="btnques" onclick="location.href='/add_post'">Post a question!</buton>
		</div>
		% end
		<div class="dvorder">
			<div class="orderTitle">Users</div>
			% for user in users:
			<div class="users">
				<image class="userface" src="../img/avatar.gif" />
				<div class="dvuser">
					<div class="userTitle">{{user["username"]}}</div>
				</div>
			</div>
			% end
		</div>
	</div>

</div>
<script type="text/javascript" src="../js/jquery-1.7.2.js"></script>
<script type="text/javascript">
	$(function()
	{

		$(".tabheads").click(function()
		{
			$(".tabheads").removeClass("tabcurrent").eq($(this).index()).addClass("tabcurrent");
			$(".tab").hide().eq($(this).index()).show();
		});
	});
</script>
</body>
</html>
