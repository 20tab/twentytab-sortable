jQuery(function(){


    //EVERY INLINE-GROUP NEEDS A SPECIFIC CLASS
	$('.inline-group').each(function(index){
        if($(this).find('.tabular').length > 0 && $(this).find('.field-position').length > 0){
            $(this).addClass('sortable-tabular-inline');
        }
        else if($(this).find('.inline-related fieldset.module .field-position').length > 0){
            $(this).addClass('sortable-stacked-inline');
            $(this).find('.inline-related').addClass('inline-sortable-item');
		}
    });

    var temp_html_bottom = "";
    //EVERY TABULAR INLINE NEEDS TO BE SORTABLE
    $('.sortable-tabular-inline').each(function(index){
        $(this).find('tbody tr').addClass('inline-sortable-item');
        $(this).find('tbody').sortable({
            cancel:".add-row",
            axis: 'y',
            delay: '150',
            start: function(event,ui){
                temp_html_bottom = $(this).find('.add-row');
                $(this).find('.add-row').remove();
            },
            stop: function(event,ui){
                $(this).append(temp_html_bottom);
                $(this).find("input,textarea,select")
                    .bind('mousedown.ui-disableSelection selectstart.ui-disableSelection', function(e) {
                    e.stopImmediatePropagation();
                });
            },
            update: function(event, ui) {
                var item = ui.item;
                var items = $(this).find('tr').get();
                $(items).each(function(index) {
                    var input = $(this).find('.field-position>input');

                    input.attr('value', index+1);
                });
                $(this).find('tr').removeClass('row1').removeClass('row2');
                $(this).find('tr:even').addClass('row1');
                $(this).find('tr:odd').addClass('row2');
            }

        });

       $(this).find('tbody').bind('sortupdate', reorder);
       $(this).find("input,textarea,select")
			.bind('mousedown.ui-disableSelection selectstart.ui-disableSelection', function(e) {
      		e.stopImmediatePropagation();
       });
    });


    //EVERY STACKED INLINE NEEDS TO BE SORTABLE
    $('.sortable-stacked-inline').each(function(index){
        $(this).find('tr').addClass('inline-sortable-item');
        $(this).sortable({
            cancel:".add-row,h2",
            axis: 'y',
            delay: '150',
            items: '.inline-related',
            stop: function(event,ui){
                $(this).find("input,textarea,select")
                    .bind('mousedown.ui-disableSelection selectstart.ui-disableSelection', function(e) {
                        e.stopImmediatePropagation();
                    });
            },
            update: function(event, ui) {
                var item = ui.item;
                var items = $(this).find('.inline-related').get();
                $(items).each(function(index) {
                    // input = $(this).find('.field-position>input');
                    var input = $(this).find('.field-position').find("input");
                    input.attr('value', index+1);
                });
                $(this).find('tr').removeClass('row1').removeClass('row2');
                $(this).find('tr:even').addClass('row1');
                $(this).find('tr:odd').addClass('row2');
            }

        });
        $(this).bind('sortupdate', reorder);
        $(this).find("input,textarea,select")
			.bind('mousedown.ui-disableSelection selectstart.ui-disableSelection', function(e) {
      		e.stopImmediatePropagation();
        });
    });


    function reorder(){

        if($(this).parents('.inline-group').hasClass('sortable-tabular-inline')){
            $(this).find('.form-row').not('.empty-form').each(function(index){
                $(this).find('.field-position>input').val(index+1);
            });
        }
        else if($(this).hasClass('sortable-stacked-inline')){
            $(this).find('.inline-sortable-item').not('.empty-form').each(function(index){
                $(this).find('.field-position>input').val(index+1);
            });
        }
    }


    $('.add-row a').on('click',function(){
        var parent = $(this).parents('.inline-group');
        if(parent.hasClass('sortable-tabular-inline')){
            parent.find('.ui-sortable').find("input,textarea,select")
                .bind('mousedown.ui-disableSelection selectstart.ui-disableSelection', function(e) {
                    e.stopImmediatePropagation();
            });
            parent.find('.ui-sortable').trigger('sortupdate');
        }
        else if(parent.hasClass('sortable-stacked-inline')){
            parent.find("input,textarea,select")
                .bind('mousedown.ui-disableSelection selectstart.ui-disableSelection', function(e) {
                    e.stopImmediatePropagation();
            });
            parent.trigger('sortupdate');
        }

	});

});
