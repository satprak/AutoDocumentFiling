$( function() {
    function split( val ) {
        return val.split(/,/ );
    }

    $( "#product" )
        // don't navigate away from the field on tab when selecting an item
        .on( "keydown", function( event ) {
            if ( event.keyCode === $.ui.keyCode.TAB &&
                    $( this ).autocomplete( "instance" ).menu.active ) {
                event.preventDefault();
            }
        })
        .autocomplete({
            minLength: 0,
            source: "{% url 'autocomplete' %}",
            focus: function() {
                // prevent value inserted on focus
                return false;
            },
            select: function( event, ui ) {
                // var terms = split( this.value );
                // console.log(this.value);
                // console.log(typeof this.value)
                var cur = this.value;
                console.log(cur)
                var index;
                for(let i=cur.length-1;i>=0;i--){
                    if(cur[i]=='+'||cur[i]=='-'||cur[i]=='|'){
                        index=i;
                        break;
                    }
                }
                cur=cur.slice(0,index+1);
                // console.log(typeof cur);
                for(let i = 0;i<ui.item.value.length;i++){
                    cur=cur+ui.item.value[i];
                }
                this.value = cur
                return false;
            }
        });
} );