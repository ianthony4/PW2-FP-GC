(function(window, $, _) {
    /*
     * :::: CONTAINERS :::: END
     */
    // Notese como se reciclan los selectores para hacer el menor
    // numero de consultas al DOM.
 
    var $containerBusqueda = $("#paso-1");
    var $containerGenerar = $("#paso-2");
    var $containerPreview = $("#paso-3");
 
    var $formEmail = $("#email-send");
    var $formBusqueda = $containerBusqueda.find('form');
    var $formByPass = $("#bypassForm");
 
    var $modalPreloader = $containerBusqueda.find('#modalPreloader');
    var $formGenerar = $containerGenerar.find('form');
    var $alertGratuito = $formGenerar.find('#gratuitoAlertMsg');
 
    var $btnBuscar = $formBusqueda.find('#enviar');
    var $btnValidar = $formBusqueda.find('#validar');
   
    var $btnReturn = $('#btnRegresar');
 
    var $btnEmitir = $containerPreview.find('#btnEmitir');
    var $btnReload = $containerPreview.find('#btnReload');
 
    var $label_si = $('#label_si');
 
	var $modalMensajes = $('#modalMensajes');
 
    
/* ajuste fecha vencimiento */
  

    var $modalDatepicker = $('#modalDatepicker');
    var $desdeField = $('#txtFec_desde');
    var $hastaField = $('#txtFec_hasta');
    var $_porcentajeRetencion = $('#porcentaje');
    var $_textoRetencion = $('#Retexto');



var _minDate = new Date();

    var des = $modalDatepicker.find("#datepicker-desde");
    des.datepicker({
        endDate: new Date(),
        startDate: new Date('2000-01-01 00:00')
    }).on('changeDate', function (e) {
        $desdeField.val([e.date.getDate() < 10 ? '0' + (e.date.getDate()) : e.date.getDate(), e.date.getMonth() < 9 ? '0'+(e.date.getMonth()+1) : (e.date.getMonth()+1), e.date.getFullYear()].join('/'));
        ajustarFechaMaxima(e.date);
        var anio = parseInt(e.date.getFullYear());

        

        if (anio>=2015)
        {   
            $_porcentajeRetencion.val('0.08');
            $_textoRetencion.text('8');
        }

        else
            {
                 $_porcentajeRetencion.val('0.10');
                 $_textoRetencion.text('10');

            }


             calcular_total();
             $hastaField.val('');

           $modalDatepicker.modal('hide');  


    });


    
    var has = $modalDatepicker.find("#datepicker-hasta");

    has.datepicker({
       
        startDate: new Date('2000-01-01 00:00')
    }).on('changeDate', function (e) {


       
        $hastaField.val([e.date.getDate() < 10 ? '0'+(e.date.getDate()) : e.date.getDate(), e.date.getMonth() < 9 ? '0'+(e.date.getMonth()+1) : (e.date.getMonth()+1), e.date.getFullYear()].join('/'));
        ajustarFechaMinima(e.date);
        $modalDatepicker.modal('hide');
    


    });

    function ajustarFechaMaxima(selectedDate) {
        
        var priorDate = new Date(selectedDate);
        var today = new Date();
        
      

        has.data('datepicker').setStartDate(selectedDate);



      

    }

    function ajustarFechaMinima(selectedDate) {
     

        des.data('datepicker').setEndDate(_minDate);

      
    }





    $('.datepicker-modal').on('click', function (e) {


        
        var $self = $(e.target).closest('.datepicker-modal');
        des.toggleClass('hidden', !$self.hasClass('desde'));
        has.toggleClass('hidden', !$self.hasClass('hasta'));
        $modalDatepicker.modal('show');
        
       

        

    });

    

   
 
 
 
/* fin fecha de vencimiento */

    /*
     * :::: CONTAINERS :::: / END
    */
 
    /*
     * :::: ELEMENTOS CRUCIALES (mas que todo, form-controls) :::: START
     */
 
    // BUSQUEDA - START


    var $numeroSerie = $formBusqueda.find('#txtNumeroSerie');
    var $numeroRecibo= $formBusqueda.find('#txtNumeroRecibo');
    
    



    var $tipoDocField = $formGenerar.find('#selTipodocide');
    var $numDocField = $formGenerar.find('#txtNumdocide');
    var $nombreClienteField = $formGenerar.find('#txtNombrecliente');
  
    var $_miDocField = $formGenerar.find('#hiddenMidocumento');
    var $_miRucField = $formGenerar.find('#hiddenMiRuc');
 
    // BUSQUEDA - / END
 
    // GENERAR - START
    var $tipoDoc = $formGenerar.find('#tipo_doc');
    var $numDoc = $formGenerar.find('#numero_doc');
    var $nombreCliente = $formGenerar.find('#razon_social');
 
    var $motivo = $formGenerar.find('#txtMotivo');
    var $observacion = $formGenerar.find('#txtObservacion');
 
    var $retencionRadioSi = $('#rbtnIndretencion_si');
    var $retencionRadioNo = $('#rbtnIndretencion_no');
 
    var $gratuitoRadioSi = $formGenerar.find('#rbtnIndgratuito_si');
    var $gratuitoRadioNo = $formGenerar.find('#rbtnIndgratuito_no');





 
    // capturamos de una vez con el plug aplicado.
 
    var $montoHonorario = $formGenerar.find('#txtCantidad');
    var $montoRetencion = $formGenerar.find('#txtRetencion');
    var $montoTotal = $formGenerar.find('#txtTotal');
    
    
 
 
    var _APLICA_RETENCION = true;
 
    // GENERAR - / END
 
    /*
     * :::: ELEMENTOS CRUCIALES (mas que todo, form-controls) :::: / END
     */
 
    /*
     * :::: FUNCIONES :::: START
     */
 
    function CapturaReciboHonorariosIdentidad(data) {
       
        $containerBusqueda.remove();
        $containerGenerar.removeClass('hidden');
        $_porcentajeRetencion.val(data.ret01);
        $_textoRetencion.text(data.ret01texto);
 
        $motivo.val(data.motivo);
        $observacion.val(data.motivo);
        $montoRetencion.val(data.retencion);
        $montoTotal.val(data.total);
 
   
        $tipoDoc.text(data.desctipdoc);
        $numDoc.text(data.numdoc);
        $nombreCliente.text(data.nombrecliente_ver);
        
 
        if (data.tipdoc != '6') {
              $retencionRadioSi.remove();
              $label_si.remove();
            $retencionRadioNo.prop("checked", true);
            _APLICA_RETENCION = false
        }
        calcular_total();
    }
 
    function calcular_total() {
        var honorario = parseFloat($montoHonorario.val().replace(',','')) || 0;
        var porcentaje = parseFloat($_porcentajeRetencion.val()) || 0;
 
        if (_APLICA_RETENCION)
            retencion = (honorario * porcentaje);
        else
            retencion = 0;
        var total = (honorario - retencion);
 
        $montoRetencion.val($.number(retencion, 2));
        $montoTotal.val($.number(total, 2));
    }
 
    function enviarDatosFormulario(data) {
        $containerGenerar.addClass('hidden');
        $containerPreview.removeClass('hidden');
        $(window).scrollTop(0);
 
        $containerPreview.find('#divNombre').text(data.nombre);
        $containerPreview.find('#divRuc').text('R.U.C. ' + data.numruc);
       
        $containerPreview.find('#divSerie').text(data.numserie + ' - ' +data.numdoc);
        $containerPreview.find('#divSerieMovil').text(data.numserie + ' - ' +data.numdoc);
        
        
        $containerPreview.find('#divDireccion').text(data.direccion);
        $containerPreview.find('#divRucCliente').text(data.numdocide);
        $containerPreview.find('#divTipo').text(data.desctipdoc);
        $containerPreview.find('#divTelefono').html('<b>Telefono:</b> ' + data.telefono);
        $containerPreview.find('#divCliente').html('<b>Recib&iacute; de: </b>' + data.nombrecliente_ver);
       
        $containerPreview.find('#divDomicilioCliente').html('<b>Domicilado en: </b>' + data.domiciliocliente);
        
        $containerPreview.find('#divConcepto').html('<b>Por concepto</b> ' + data.motivo);
        $containerPreview.find('#divMonto').html('<b>La suma de</b> ' + data.cantidadletra);
        $containerPreview.find('#divObservacion').html('<b>Observaci&oacute;n</b> ' + data.observacion);


         //'<b>Observaci&oacute;n</b> ' + data.observacion;

        $ind_estado_rec=data.ind_estado_rec;
        if ($ind_estado_rec==2)
        $containerPreview.find('#divAnulado').html('Anulado');

        

        $containerPreview.find('#divInciso').html('<b>Inciso</b>' + ' "' + data.indrenta + '"' + ' DEL ART&Iacute;CULO 33 DE LA LEY DEL IMPUESTO A LA RENTA ');
        $containerPreview.find('#divFecha').html('<b>Fecha de Emisi&oacute;n</b> ' + data.diafechaemi + '<b> de </b>' + data.mesletras + ' <b> de </b> ' + data.aniofechaemi);
        

        $containerPreview.find('#divFechaVencimiento').html(data.htmlFechavencimiento );
        
        $containerPreview.find('#divTotalHonorarios').text($.number(data.cantidad, 2));
        $containerPreview.find('#divRetencion').text($.number(data.retencion, 2));
        $containerPreview.find('#divTotalRecibido').text($.number(data.total, 2) + ' ' + data.desmoneda);
 
        $containerPreview.find('#divGratuito').text(data.desgratuito);
        $containerPreview.find('#divtipoNumero').html('<b>Identificado con</b> ' + data.desctipdoc + ' n&uacute;mero ' + data.numdocide);
        $containerPreview.find('#divRetexto').html(data.ret01texto);
 
 
 
 
        $containerPreview.find('#divTotalHonorarios2').text($.number(data.cantidad, 2));
        $containerPreview.find('#divRetencion2').text($.number(data.retencion, 2));
        $containerPreview.find('#divTotalRecibido2').text($.number(data.total, 2) + ' ' + data.desmoneda);
        $containerPreview.find('#divRetexto2').html(data.ret01texto);
 
 

 
 
    }
 
  
   



  
  


 
   
 
    $btnReload.on('click', function () {
        $numDocField.val('');
        $tipoDocField.val('');
        $nombreCliente.val('');
        $(".lista-errores").remove()
    })
 
    $tipoDocField.on('change', function(e) {

        $numDocField.val('').closest('.form-group').removeClass('help-block');
        $nombreClienteField.val('').closest('.form-group').removeClass('help-block');
        $numDocField.data('pivot-valid', '1');
        
         $retencionRadioNo.prop('checked', true).trigger('change');
         $retencionRadioSi.attr('disabled', 'disabled');


        var length = 12;
        if (e.target.value == "6")
            {
                length = 11;

                _APLICA_RETENCION = true;
                $retencionRadioSi.removeAttr('disabled');
                $retencionRadioSi.prop('checked', true).trigger('change');
                 calcular_total();
               
                
            }

        if (e.target.value == "1")
            length = 8;
        


        $numDocField.attr('maxlength', length);
        $(".lista-errores").remove();
 
    });



    $motivo.on('change', function(e) {
        e.target.value = (e.target.value + '').toUpperCase();
    })
    $observacion.on('change', function(e) {
        e.target.value = (e.target.value + '').toUpperCase();
    })
 
    $gratuitoRadioSi.on('change', function(e) {
        $alertGratuito.removeClass('hidden');
        $retencionRadioNo.prop('checked', true).trigger('change');
        $retencionRadioSi.attr('disabled', 'disabled');
    });
 
    $gratuitoRadioNo.on('change', function(e) {
        $alertGratuito.addClass('hidden');
        $retencionRadioSi.removeAttr('disabled');
    });
 
    $retencionRadioNo.on('change', function(e) {
        _APLICA_RETENCION = false;
        calcular_total();
    });
 
    $retencionRadioSi.on('change', function(e) {
        _APLICA_RETENCION = true;
        calcular_total();
    });
 
    $montoHonorario.on('change blur focus', function(e) {
        calcular_total();
    });
 
    $btnReturn.bind('click', function(e) {
        $containerPreview.addClass('hidden');
        $containerGenerar.removeClass('hidden');
        console.log('activo');
    });
 
    $containerGenerar.find('[data-toggle="popover"]').on('click', function(e) {
        e.preventDefault();
    });
 
 
     


$formByPass.submit(function(e){
    
    $(this).children('input[type=submit]').attr('disabled', 'disabled');
     $btnReturn.prop('disabled', true);
    
    
   
});







    $formGenerar.validate({
       //  onkeyup: false,
      //  onchange: false,
      //  onclick: false,
      //  onfocusout: false,


        rules: {

            txtFec_desde: {
                required: true
            },

             selTipodocide: {
                required: true
            },


             txtNumdocide: {
                required: {
                    depends: function(element) {
                        return $tipoDocField.val() != "" && $tipoDocField.val() != "-";
                    }
                },
                validStr: true,
                validRUC: {
                    depends: function(element) {
                        return $tipoDocField.val() == "6";
                    }
                },
                minlength: {
                    param: function (element) {
                        if($tipoDocField.val() == "1")
                            return 8;
                        else if($tipoDocField.val() == "6")
                            return 11;
                        else
                            return 1;
                    }
                },
                maxlength: {
                    param: function (element) {
                        if($tipoDocField.val() == "1")
                            return 8;
                        else if($tipoDocField.val() == "6")
                            return 11;
                        else
                            return 12;
                    }
                },
                digits: {
                    depends: function(element) {
                        return $tipoDocField.val() == "1" || $tipoDocField.val() == "6";
                    }
                },
                notEqual: {
                    param: function() {
                        if ($tipoDocField.val() == "1")
                            return $_miDocField.val()
                        if ($tipoDocField.val() == "6")
                            return $_miRucField.val()
                    },
                    depends: function() {
                        return $tipoDocField.val() == "1" || $tipoDocField.val() == "6";
                    }
                }
            },

            


             txtNombrecliente: {
                required: true,
                minlength: 2,
                validStr: true
            },
       





            txtNumeroSerie: {
                required: true,
                minlength: 4,
                maxlength:4
                
            },

               txtNumeroRecibo: {
                required: true,
                minlength: 1,
                maxlength: 9
                
            },

            txtMotivo: {
                required: true,
                minlength: 5,
                validStr: true
            },
            txtObservacion: {
                validStr: true
            },
            txtCantidad: {
                required: true,

                minimo: 0,
				maxlength:13



                    
            }








        },




        messages: {



              txtFec_desde: {
                required: "Debe seleccionar la fecha de emisi&oacute;n"
            },

            txtNumdocide: {
                notEqual: function() {
                    if ($tipoDocField.val() == "6")
                        return "El usuario del servicio debe ser diferente al emisor"
                    if ($tipoDocField.val() == "1")
                        return "El usuario del servicio debe ser diferente al emisor"
                    return "not-equal";
                },
                // valid_pivot: "Invalid PIVOT!!",            
                digits: function() {
					
                   // $nombreClienteField.addClass('hidden');
                    if ($tipoDocField.val() == "6")
                        return "El n&uacute;mero de RUC no es v&aacute;lido"
                    if ($tipoDocField.val() == "1")
                        return "El documento ingresado no existe"
                    return "digits";
                },
                required: function() {
                    if ($tipoDocField.val() == "6")
                        return "El n&uacute;mero de RUC no es v&aacute;lido"
                    if ($tipoDocField.val() == "1")
                        return "Ingrese el n&uacute;mero de documento "
                    return "Ingrese el n&uacute;mero de documento de identidad del usuario";
                },
               
            }
        },


        /*** FIX ATTEMPT **/
        invalidHandler: function (event, validator) {
            var offset = $(validator.errorList[0].element).offset();
            $(window).scrollTop(offset.top - 30);
        },
        /*** END / FIX ATTEMPT **/
        submitHandler: function(form) {
            var formData = $(form).serializeObject();
            var url = 'registro4ta.do?action=capturaRecibo4ta';
            //var url = 'a/json/resp.json';
            
			/*
            var honorario = Number($montoHonorario.val());
 
            if (honorario <= 1500 && $retencionRadioSi.is(':checked')) {
                alert("Si el monto es menor o igual a 1500.00, entonces no se puede hacer retencion, salvo que haya iniciado sus retenciones y/o pagos a cuenta.");
            }
		*/
            $.ajax({
                url: url,
                data: formData,
                contentType: "application/json; charset=utf-8",
                dataType: 'json',
                success: function(data) {
					
					var msj=data.mensajeerror + ' ' + data.mensajesol;
					
                    if (data.errorval==1){
                   	 
                     $('#divMensaje').text(msj);
					 console.log(msj);
					 $modalMensajes.modal('show');
					}
                    else
					{
                    
					if (data.errorval==2)
					
						{
							 $('#divMensaje').text(msj);
							 console.log(msj);
							 $modalMensajes.modal('show');
							
						}
						
						enviarDatosFormulario(data);
                    
					}

                },

               

                error: function(xhr,status,error) {
                    
                    var data=jQuery.parseJSON(xhr.responseText);
                    console.log(data.total.mensajerror+' '+data.total.mensajesol);



                    }
                   

                });
        }
    });




    /*
     * :::: FORM VALIDATE :::: / END
     */
 
    $formEmail.validate(_.extend(window._validatorWallSettings, {
        rules: {
            txtEmail: {
                required: true,
                email: true,
				regex: /\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b/i 
            }
        },
        submitHandler: function(form) {
            var formData = $(form).serializeObject();
            var url = 'registro4ta.do?action=enviarCorreo';
            $.ajax({
                method: 'post',
                url: url,
                data: formData,
                success: function() {
 
                    alert('El correo fue enviado.');
 
                    $("#txtEmail").val();
                },
                error: function() {
                    alert('Error al enviar el correo.');
                }
            });
        }
    }));
 
    /*
     * :::: SETUP :::: START
     */
 
    $modalPreloader.modal({
        backdrop: 'static',
        keyboard: false,
        show: false
    });
 
    $containerGenerar.find('[data-toggle="popover"]').popover()
 
    
 

    $btnBuscar.hide();
    $btnValidar.hide();
 
    /*
     * :::: SETUP :::: / END
     */
    
    $("[data-toggle]").on('click', function (e) {
        e.preventDefault();
    });
 
})(window, jQuery, _);