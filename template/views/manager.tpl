<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Manage</title>
    <style>
        body {
            overflow: hidden;
        }

        * {
            margin: 0;
            font-family: "Microsoft Yahei";
            color: #666;
        }

        div {
            margin: auto;
            margin-bottom: 10px;
            margin-top: 10px;

        }

        #header {
            height: 82px;
            width: 1200px;
        }

        #main {
            height: 460px;
            width: 1200px;
            border: 1px black solid;
            overflow: auto;
        }

        .book_info div {
            height: 10px;
            width: 300px;
            text-align: left;
        }

        .wel_word {
            font-size: 60px;
            float: left;
        }
        #header div a {
            text-decoration: none;
            font-size: 20px;
        }

        #header div {
            float: right;
            margin-top: 55px;
        }


        .book_cond input {
            width: 50px;
            text-align: center;
        }

        #main table{
            margin: auto;
            margin-top: 80px;
            border-collapse: collapse;
        }

        #main table td{
            width: 120px;
            text-align:center;
            border-bottom: 1px #e3e3e3 solid;
            padding: 10px;
        }

        .user_info{
            width: 700px;
            text-align: right;
        }

        .user_span {
            margin-left: 20px;
        }

        .user_span span{
            color: red;
            font-size: 20px;
            margin: 10px;
        }

        .user_span a , td a{
            font-size: 20px;
            color: blue;
        }

        #header div span {
            margin: 10px;
        }

        #header div .um_span{
            color: red;
            font-size: 25px;
            margin: 10px;
        }

        #header div a {
            color: blue;
        }
    </style>

</head>
 % include('/home/yunqi/git_version/INFO2222-Group-Project/template/views/header.tpl')

<body>
	<div id="header">
			<span class="wel_word">Welcome Admin</span>

	</div>
	
	<div id="main">
	
		<table>

			<tr>
			    <td>UserId</td>
				<td>Username</td>
				<td>Password</td>
				<td>Email</td>
			</tr>
			% for user in users:
			<tr>
			    <td>{{user["user_id"]}}</td>
			    <td>{{user["username"]}}</td>
				<td>{{user["password"]}}</td>
				<td>{{user["email"]}}</td>
				<td><a id="delete" href="/manager/{{user["user_id"]}}">Delete</a></td>
				<td><a id="mute" href="/manager/mute/{{user["user_id"]}}">Mute</a></td>
				<td><a id="unmute" href="/manager/unmute/{{user["user_id"]}}">Unmute</a></td>
			</tr>
		    % end
		</table>
		<div class="user_info">
			<span class="user_span">There are<span class="b_count">{{count}}</span>users</span>
			<span id= "clear" class="user_span"><a href="/manager/all">Clear all users!</a></span>
			<span class="user_span"><a href="/add_user">Add user!</a></span>
		</div>
	</div>
	<script type="text/javascript" src="js/jquery-1.7.2.js"></script>
	<script type="text/javascript">
			$("#delete").click(function (){
				return confirm("Are you sure to delete ?");
			})
			$("#mute").click(function (){
				return confirm("Are you sure to mute ?");
			})
			$("#unmute").click(function (){
				return confirm("Are you sure to unmute ?");
			})
			% if len(users)!=0:
			$("#clear").click(function (){
				return confirm("Are you sure to delete all users?");
			})
			% end
	</script>

</body>
</html>