// Para prevenir 'ReferenceError console is not defined'.
(function(window, _, $) {
    var metodo;
    var noop = function () {};
    // noop -> no-op -> una funciÃ³n vacÃ­a para mantener funcionalidad.
    var metodos = [
        'assert', 'clear', 'count', 'debug', 'dir', 'dirxml', 'error',
        'exception', 'group', 'groupCollapsed', 'groupEnd', 'info', 'log',
        'markTimeline', 'profile', 'profileEnd', 'table', 'time', 'timeEnd',
        'timeStamp', 'trace', 'warn'
    ];
    var total_metodos = metodos.length;
    var console = (window.console = window.console || {});

    while (total_metodos--) {
        metodo = metodos[total_metodos];
        // Solo estandarizar metodos inexistentes.
        if (!console[metodo]) {
            console[metodo] = noop;
        }
    }

    if(_){
        _.templateSettings = {
            evaluate    : /\{\{\:([\s\S]+?)\}\}/g,
            interpolate : /\{\{([\s\S]+?)\}\}/g,
            escape      : /\{\{\-([\s\S]+?)\}\}/g
        };
    }

    $.fn.serializeObject = function () {
        var array = this.serializeArray();
        var obj = {};
        array.forEach(function(e){
            obj[e.name] = e.value;
        })
        return obj;
    }

  
    String.prototype.format = function() {
        var args = arguments;
        return this.replace(/{(\d+)}/g, function(match, number) { 
            return typeof args[number] != 'undefined' ? args[number] : match;
        });
    };


    function validRUC(valor) {
        var valor = valor.trim();
        if (/\d/g.test(valor)) {
            if (valor.length == 8) {
                suma = 0
                for (i = 0; i < valor.length - 1; i++) {
                    digito = valor.charAt(i) - '0';
                    if (i == 0) suma += (digito * 2)
                    else suma += (digito * (valor.length - i))
                }
                resto = suma % 11;
                if (resto == 1) resto = 11;
                if (resto + (valor.charAt(valor.length - 1) - '0') == 11) {
                    return true
                }
            } else if (valor.length == 11) {
                suma = 0
                x = 6
                for (i = 0; i < valor.length - 1; i++) {
                    if (i == 4) x = 8
                    digito = valor.charAt(i) - '0';
                    x--
                    if (i == 0) suma += (digito * x)
                    else suma += (digito * x)
                }
                resto = suma % 11;
                resto = 11 - resto
                if (resto >= 10) resto = resto - 10;
                if (resto == valor.charAt(valor.length - 1) - '0') {
                    return true
                }
            }
        }
        return false
    }

    window.numberVal = function ( value ) {
        value = parseFloat(value);
        if(value != +value || value == +Infinity || value == -Infinity)
            return 0;
        else
            return value;
    }
	
	
	
	
	
	

    function ValidaCadena(sCadena, sCampo){
        var i =0 ;
        var sCaracteres ="/|{}$%/=?[]^~!#Â¿Â¬Â°Â¨Â¡`";
        while ( i < sCadena.length ) {                    
            caracter = sCadena.charAt(i);    
            if ( caracter=="&"  && (i ==0 || i==sCadena.length-1 ))
            {
                return 2;
                return false;
            }
           
            if (caracter=="\\" || caracter=="\"" ){
                return 3;
                return false;
            }else{
                if ( sCaracteres.indexOf( caracter ) != -1 ) {     
                    return 4;
                }   
            }
            i++;                                        
        }
        return 1;
    }

    var datepickerConfig = {
      format: 'dd/mm/yyyy',
      todayBtn: false,
      language: "es",
      autoclose: true,
      todayHighlight: true
    };
    
    if($.fn.datepicker)    
        $.fn.datepicker.defaults = $.extend($.fn.datepicker.defaults, datepickerConfig);
    
    if(!$.validator)
        return;
    
    window._validatorWallSettings = {
        errorClass: 'error',
        errorElement: 'span',
        wrapper: 'li',
        errorWall: '.lista-errores',
        showErrors: function (errorMap, errorList) {
            var wall = $(this.currentForm).find(this.settings.errorWall);
            if(wall.length == 0){
                wall = $('<div/>').addClass(this.settings.errorWall.substr(1)).prependTo(this.currentForm);
            }
            if(this.numberOfInvalids() == 0)
                wall.addClass('hidden');
            else
                wall.removeClass('hidden');

            this.defaultShowErrors();
        },
        errorPlacement: function(error, element) {
            var wall = $(this.currentForm).find(this.settings.errorWall);
            if(wall.length == 0){
                wall = $('<div/>').addClass(this.settings.errorWall.substr(1)).prependTo(this.currentForm);
            }
            var alert = wall.find('.alert');
            if(alert.length == 0){
                alert = $('<div/>').addClass('alert alert-danger');
                alert.appendTo(wall);
            }
            error.appendTo(alert);
        }
    };

    $.validator.setDefaults({
        highlight: function(element, errorClass) {
            $(element).closest('.form-group').addClass('has-error');
        },
        unhighlight: function(element, errorClass) {
            $(element).closest('.form-group').removeClass('has-error');
        },
        errorClass: 'help-block',
        errorElement: 'span',
        showErrors: function () {
            //$(this.currentForm).find('.has-error').removeClass('has-error');
            this.defaultShowErrors();
        },
        /*
        onkeyup: false,
        onchange: false,
        onclick: false,
        onfocusout: false,
        */
        ignore: '[type="hidden"]',
        errorPlacement: function(error, element) {
            if(element.parent('.input-group').length) {
                error.insertAfter(element.parent());
            } else {
                error.insertAfter(element);
            }
        },
        startOnInit: true
    });

    $.validator.addMethod("notEqual", function(value, element, param) {
      return value != param;
    }, "Please specify a different (non-default) value");

    $.validator.addMethod("equal", function(value, element, param) {
        
      return value == param;
    }, "not-equals");
	
	/*
	METODO ACTUALIZADO VALIDACION CORREO
	*/
	$.validator.addMethod(
        "regex",
        function(value, element, regexp)  {
            if (regexp.constructor != RegExp)
                regexp = new RegExp(regexp);
            else if (regexp.global)
                regexp.lastIndex = 0;
            return this.optional(element) || regexp.test(value);
        });
		
	
	
		

    $.validator.addMethod("lessThan", function(value, element, param) {
        
        var i = parseFloat(value);
        var j = parseFloat(param);
        return i <= j;
    }, "The value must be less than {0}");
    
    $.validator.addMethod("validRUC", function(value, element, param) {
        var valid = validRUC(value);
        $(element).data('validRUC', valid ? '1' : '0');
      return valid;
    }, "El n&uacute;mero de ruc no es v&aacute;lido");
	
	
	
	
	

    /// ESTA REGLA DE VALIDACION (que no es una regla per se)
    /// ROMPE CON TODO EL PATRON DE TRABAJO DEL PLUGIN
    /// MANIPULAR CON CUIDADO TODO ESTA HARDCODED
    ////return /^([a-z0-9\s\xe1\xe9\xed\xf3\xfa\xf1\xfc\-\+\.\&\,\;]+)?$/ig.test(value);
    //// el 2016-03-04  NAA  se esta agregando \/\(\)\#\'\"

    $.validator.addMethod("validStr", function(value, element, param) {
        return /^([a-z0-9\s\xe1\xe9\xed\xf3\xfa\xf1\xfc\-\+\.\&\/\(\)\#\'\"\,\;]+)?$/ig.test(value);
    },"Los caracteres ingresados no son v&aacute;lidos. ");

    $.validator.addMethod("serie_doc", function(value, element, params) {
        return /^(E001)?$/ig.test(value);
    }, "El numero de serie del recibo electr&oacute;nico o de los otros ingresos de cuarta debe iniciar con la letra E");

    $.validator.addMethod("num_serie_doc", function(value, element, params) {
        return /^((E001)|(\d+))?$/ig.test(value);
    }, "El numero de serie debe iniciar con la letra E y/o solo contener dÃ­gitos");

     $.validator.addMethod("validpivot", function(value, element, params) {
        
        return $(element).data('pivot-valid') == '1';
    }, "pivot-wrong!");
    
    $.validator.addMethod("non_repeated", function(value, element, params) {
        var d = {};
        [].forEach.call(value, function (e) {
            d[e] = d[e]+1 || 1;
        });
        return _.size(d) > 1;
    }, "El n&uacute;mero de serie no es v&aacute;lido");

    $.validator.addMethod("minimo", function(value, element, params) {
        var val = parseFloat(value.replace(',' ,''));
        return !isNaN(val) && val > params;
    }, "Debe ingresar un monto mayor a 0.00");

}(window, _, jQuery));