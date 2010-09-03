jQuery(function(){
	
	// Header Menu
	$("#header-menu-wrapper-main").html($("#header-menu").html() + '<div class="clear">&nbsp;</div>')
	$("#header-menu .active-head h2 a").click(function(){
		if($(this).hasClass("active-hover")){
			$("#header-menu-wrapper").hide();
			$(this).removeClass("active-hover");

		}else{
			$("#header-menu-wrapper").show();
			$(this).addClass('active-hover')
		}
		return false;
	});
	$("html").click(function(){
			$(".active-head").removeClass("active-hover");
			$("#header-menu-wrapper").hide();
			
	});

	// Buttons
	$(".btn").button();
})
