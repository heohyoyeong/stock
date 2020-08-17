jQuery('#selectBox').change(function() {
	var state = jQuery('#selectBox option:selected').val();
	if ( state == 'gs' ) {
		jQuery('.layer').show();
	} else {
		jQuery('.layer').hide();
	}
});