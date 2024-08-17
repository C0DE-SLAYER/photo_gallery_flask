'use strict';

$(window).on('load', function() {

	/*------------------
		filter to active
	--------------------*/
	$('.filter-controls li').on('click', function() {
		$('.filter-controls li').removeClass('active');
		$(this).addClass('active');
	});

	if($('.gallery__warp').length > 0 ) {
		var containerEl = document.querySelector('.gallery__warp');
		mixitup(containerEl);
	}

});

(function($) {

	/*------------------
		Background Set
	--------------------*/
	$('.set-bg').each(function() {
		var bg = $(this).data('setbg');
		$(this).css('background-image', 'url(' + bg + ')');
	});
})(jQuery);

