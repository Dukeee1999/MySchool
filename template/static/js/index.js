$(function(){
	var stuList = getStuList();

	$('input').eq(0).focus(function(){
		if($(this).val().length==0){
			$(this).parent().next("div").text("Support word and number");
		}
	})
	$('input').eq(1).focus(function(){
		if($(this).val().length==0){
		    $(this).parent().next("div").text("Recommand for combining words and number");
		}
	})
	$('input').eq(2).focus(function(){
		if($(this).val().length==0){
			$(this).parent().next("div").text("Reenter the password");
		}
	})

	//input各种判断
	//username:
	$('input').eq(0).blur(function(){
		if($(this).val().length==0){
			$(this).parent().next("div").text("");
			$(this).parent().next("div").css("color",'#ccc');
		}else if($(this).val().length>0 && $(this).val().length<4){
			$(this).parent().next("div").text("Length should be in 4-20");
			$(this).parent().next("div").css("color",'red');
		}else if($(this).val().length>=4&& !isNaN($(this).val())){
			$(this).parent().next("div").text("Username can not all be number");
			$(this).parent().next("div").css("color",'red');
		}
	})
	//password
	$('input').eq(1).blur(function(){
		if($(this).val().length==0){
			$(this).parent().next("div").text("");
			$(this).parent().next("div").css("color",'#ccc');
		}else if($(this).val().length>0 && $(this).val().length<6){
			$(this).parent().next("div").text("The length should be within 6-20");
			$(this).parent().next("div").css("color",'red');
		}else{
			$(this).parent().next("div").text("");
		}		
	})
//	confirm password
	$('input').eq(2).blur(function(){
		if($(this).val().length==0){
			$(this).parent().next("div").text("");
			$(this).parent().next("div").css("color",'#ccc');
		}else if($(this).val()!=$('input').eq(1).val()){
			$(this).parent().next("div").text("Two password did not match");
			$(this).parent().next("div").css("color",'red');
		}else{
			$(this).parent().next("div").text("");
		}		
	})
//	submit btn
	$("#submit_btn").click(function(e){		
		for(var j=0 ;j<5;j++){
			if($('input').eq(j).val().length==0){				
				$('input').eq(j).focus();
				$('input').eq(j).parent().next(".tips").text("This place can not be empty");
				$('input').eq(j).parent().next(".tips").css("color",'red');
				e.preventDefault();
				return;
			}
			if(j==0){
				if($('input').eq(j).val().length>0&& $('input').eq(j).val().length<4){
					e.preventDefault();
					return;
				}else if($('input').eq(j).val().length>=4&& !isNaN($('input').eq(j).val())){
					e.preventDefault();
					return;
				}
			}
			if(j==1){
				if($('input').eq(j).val().length>0&& $('input').eq(j).val().length<6){
					e.preventDefault();
					return;
				}
			}
			if(j==2){
				if($('input').eq(j).val()!= $('input').eq(1).val()){
					e.preventDefault();
					return;
				}
			}
		}
	})

	function Student(name,password,tel,id){
         this.name = name;
         this.password = password;
         this.tel = tel;
         this.id = id;
     }
	function getStuList(){
	    var list = localStorage.getItem('stuList');
	    if(list != null){
	        return JSON.parse(list);
	    }else{
	        return new Array();
	    }
	}

})
