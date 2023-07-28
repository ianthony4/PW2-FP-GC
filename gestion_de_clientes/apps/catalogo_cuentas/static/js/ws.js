/*Funciones movil v15-02-2020 */
/*

Ubicación: /a/js/apps/workspace/ws.js 

 */
var esAndroid=false;
var esIos=false;
var esMovil=false;
var frameAlto=0;
var frameAncho=0;
var opcionApp='';

//2017_02_08: Componente Biofacial
//Importar: <script src="/a/js/apps/workspace/ws.js"></script>
//abre camara invocar con: wsCapturaBiofacial()
//se debe implementar el retorno: "function wsRetornoFotoBiofacial(fotoBiofacial){}"
var fotoBiofacial='';
function wsCapturaBiofacial(){
	try{
		parent.postMessage("capturaFotoBiofacialWs",'*');
	}catch(ex){
		try{
			window.parent.postMessage("capturaFotoBiofacialWs",'*');
		}catch(ex){
		}
	}
}

try{
	esMovil=parent.esMovil;
}catch(ex){
	try{
		esMovil=window.esMovil;
	}catch(ex){
	}
}
var movilUrl='url';
var ag=navigator.userAgent.toLowerCase();
if (ag.indexOf("android") >= 0) {
	esAndroid = true;
}
if (ag.indexOf("iphone") >= 0 || ag.indexOf("ipad") >= 0) {
	esIos = true;
}
/*
if (ag.indexOf("android") >= 0 || ag.indexOf("iphone") >= 0 || ag.indexOf("ipad") >= 0) {
	esMovil = true;
}*/
var u=window.location.href;
if(u.indexOf("cl-ti-iagenerador")>=0){			
}else{
	$( document ).ready(function() {   	
		$("#btnVolverWorkspace").hide();
		frameIniciado();
	});
}

function iniciaMovil(){
	esMovil=true;
	
	var u=window.location.href;
	
	if(u.indexOf("ol-ti-itvisornoti")>=0 || 
	u.indexOf("cl-ti-iagenerador")>=0){	
		mainBuzon();
	}else{
		margenAbajo();
	}
	
	
	
	evaluaLogo(false);
	
	
	movilUrl=window.location.href;


	if(esAndroid){
		$("input[type='text'],input[type='number'],input[type='password'],input[type='tel'],input[type='email'], textarea").on('focus', function(event){
			 if(esAndroid){
				margenAbajo();
				var resultado=isElementInViewportHalf(this);
				if(resultado!=true){
					var ele=$(this);
					setTimeout(function(){ 
						$('html, body').animate({
							scrollTop: (ele.offset().top-100)
						}, 400);
					 }, 100);
				}
			 }    		
		 });  
		 /*$("input[type='text'],input[type='number'],input[type='password'],input[type='tel'],input[type='email'], textarea").on('focusout', function(event){
			 if(esAndroid){
				anulaMargenAbajoWs();
			 }    		
		 });*/
	}
	 
	 
	 loginEventos();

	 $("#btnVolverWorkspace").show();
	 
	$("#btn_salir").addClass("hidden");//denuncias	
	 
	 //irArriba();
	 setTimeout(function(){ 		
		frameCargado();
	 }, 500);
}
function loginEventos(){
	//menu-sso
	$("#divSignonFormLogo").hide();
	$("#divSignonFormFooter").hide();
	$("#divSignonFormCandado").hide();
	$("#aOlvidaste").hide();
	
	$("#txtUsuario").removeAttr('maxlength');
	$("#txtContrasena").removeAttr('maxlength');
	$("#txtRuc").removeAttr('maxlength');
	
	//Denuncias
	//Modificado por ccaciquey, pase PAS20181U230300018
	//$("#divPanelIv").hide();
	
	//Químicos
	$("#txtRuc").removeAttr('maxlength');
	$("#txtPlaca").removeAttr('maxlength');
	
	
}

function listenerEventos(event){
	if (event.data == 'evaluaLogo') {
		evaluaLogo(false);
	}else if (event.data == 'irArriba') {
		irArriba();
	}else if (event.data == 'esAndroid') {
		esAndroid=true;
	}else if (event.data == 'margenAbajo') {
		margenAbajo();
	}else if (event.data == 'mensajeVolver') {
		mensajeVolver();
	}else if (event.data == 'irHome') {
		irHome();
	}else if (event.data == 'irHomeRhe') {
		irHomeRhe();
	}else if (event.data == 'irHomeFactura') {
		irHomeFactura();
	}else if (event.data == 'iniciaMovil') {
		iniciaMovil();
	}else if (event.data == 'anulaMargenAbajoWs') {
		anulaMargenAbajoWs();
	}else if (event.data == 'pingWs') {
		pingWs();
	}else if (event.data == 'cerrarDescargaBuzon') {
		//alert('Cerrando progress');
		cierraDivBuzonDescarga();
	}else{			
		if (event.data.indexOf('frameIniciadoBuzon_')>=0) {
			var datos=event.data;
			
			var url=datos.substring(datos.indexOf("_")+1, datos.length) ;
			//alert(url);
			//visorPdf(url);//* //rediseñar nuevo canvas de espera
			visorPdfDescarga(url);
			
		}else if (event.data.indexOf('frameAlto_')>=0) {
			var datos=event.data;			
			frameAlto=datos.substring(datos.indexOf("_")+1, datos.length) ;
			//alert('recibido frameAlto:'+frameAlto);
			
		}else if (event.data.indexOf('frameAncho_')>=0) {
			var datos=event.data;			
			frameAncho=datos.substring(datos.indexOf("_")+1, datos.length) ;
			//alert('recibido frameAncho:'+frameAncho);
			
		}else if (event.data.indexOf('opcionApp_')>=0) {
			var datos=event.data;			
			opcionApp=datos.substring(datos.indexOf("_")+1, datos.length) ;			
		}else if (event.data.indexOf('recibeFotoBiofacialWs_')>=0) {
			//2017_02_08: Componente Biofacial
			var datos=event.data;			
			fotoBiofacial=datos.substring(datos.indexOf("_")+1, datos.length) ;	
			try{
				//localStorage.setItem("captFacial",fotoBiofacial);
			}catch(ex){
			}
			try{
				retornoFotoBiofacial(fotoBiofacial);
			}catch(ex){
			}
		}
	}
}
if(window.addEventListener){
	addEventListener("message", listenerEventos, false);
}else{
	attachEvent("onmessage", listenerEventos);
}

 
 function margenAbajo(){
	
	
	/*$("html").css("overflow",'auto'); 
	$("html").css("height",'100%'); 
	
	$("body").css("overflow",'auto'); 
	$("body").css("height",'100%'); */
	
	var mitadAlto=parseInt(window.innerHeight/2,10);   
	if(mitadAlto<100){
		mitadAlto=parseInt($("body").height()/3,10);
	}
	$("body").css("margin-bottom",''+mitadAlto+'px'); 
 }
 
 function anulaMargenAbajoWs(){
	$("body").css("margin-bottom",'0px');   
	/*if (!$(this).find("input").length) {
        alert("form empty!");
        return false;
    }*/
 }
 function isElementInViewportHalf(el) {
	var rect = el.getBoundingClientRect();
	return rect.bottom > 0 &&
		rect.right > 0 &&
		rect.left < (window.innerWidth || document.documentElement.clientWidth) /*or $(window).width() */ &&
		rect.top < (parseInt(window.innerHeight/4,10) || parseInt(document.documentElement.clientHeight/4,10)) /*or $(window).height() */;
 }	 
 function evaluaLogo(dato){
	 if(dato==true){
	 }else{
		 $("#divHeader").hide();
	 }
 }
 function irArriba(){
	 var top = $('body').scrollTop();
	 if(parseInt(top, 10)>0){
		 $('html, body').animate({
			 scrollTop: 0
		 }, 450);
		 
	 }
	 if(esAndroid){
		$('#divHeader').after('<input type="checkbox" id="focusable" style="height:0; margin-left:-200px; clear: both;" />');
		$('#focusable').focus();
		$('#focusable').remove();
	 }
 }
 function frameIniciado(){
	try{
		parent.postMessage("frameIniciado",'*');
	}catch(ex){
		try{
			window.parent.postMessage("frameIniciado",'*');
		}catch(ex){
		}
	}
	
	
	 try{
		
		if(esAndroid){
			$("#btnVolverAndroid").removeClass("hidden");					
			$("#btnVolverAndroid").bind('click',function(event){
				history.back();
				
				event.preventDefault();
				event.stopImmediatePropagation();
				return false;
			});   

			var btn1=$(".btnVolverAndroid");
			btn1.removeClass("hidden");					
			btn1.bind('click',function(event){
				history.back();
				
				event.preventDefault();
				event.stopImmediatePropagation();
				return false;
			});   

			
			$(".btnVolverAntiguo").addClass("hidden");//rhe	
			
		}else if(esIos){		
			$("#btnVolverIos").removeClass("hidden");					
			$("#btnVolverIos").bind('click',function(event){
				//TODO para ios
				
				try{
					//window.history.back()
                                        try{
					    //navigator.app.backHistory();
                                        }catch(ex){
											
                                        }
					//alert(opcionApp);								
					if(opcionApp=='appBuzon'){//buzon				
						if(u.indexOf("ol-ti-itvisornoti")>=0 ){	
							//padre ir al menu
							regresaWorkspace();
						}else if(u.indexOf("signon.htm")>=0 ){	
							window.location.href = '/ol-ti-itvisornoti/visor/master.do';
						}						
					}else{
						try{
							history.go(-1);
						}catch(ex){
						}
					}
					
					
					/*var nav = window.navigator;
					if( this.phonegapNavigationEnabled &&
						nav &&
						nav.app &&
						nav.app.backHistory ){
						nav.app.backHistory();
					} else {
						window.history.back();
					}*/
				}catch(ex){
				}
				
				event.preventDefault();
				event.stopImmediatePropagation();
				return false;
			}); 

			
			var btn2=$(".btnVolverIos");
			btn2.removeClass("hidden");					
			btn2.bind('click',function(event){
				//TODO para ios
				try{
					//window.history.back()
					 try{
					    //navigator.app.backHistory();
                                        }catch(ex){
											
                                        }
										
					//alert(opcionApp);								
					if(opcionApp=='appBuzon'){//buzon				
						if(u.indexOf("ol-ti-itvisornoti")>=0 ){	
							//padre ir al menu
							regresaWorkspace();
						}else if(u.indexOf("signon.htm")>=0 ){	
							window.location.href = '/ol-ti-itvisornoti/visor/master.do';
						}						
					}else{
						try{
							history.go(-1);
						}catch(ex){
						}
					}
					
					/*var nav = window.navigator;
					if( this.phonegapNavigationEnabled &&
						nav &&
						nav.app &&
						nav.app.backHistory ){
						nav.app.backHistory();
					} else {
						window.history.back();
					}*/
				}catch(ex){
				}
				
				
				event.preventDefault();
				event.stopImmediatePropagation();
				return false;
			}); 			

			$(".btnVolverAntiguo").addClass("hidden");//rhe	
		}
		
	}catch(ex){
	}
}
 function frameCargado(){
	try{
		parent.postMessage("frameCargado",'*');
	}catch(ex){
		try{
			window.parent.postMessage("frameCargado",'*');
		}catch(ex){
		}
	}
}
 function pingWs(){
	try{
		parent.postMessage("respuestaPingWs",'*');
	}catch(ex){
		try{
			window.parent.postMessage("respuestaPingWs",'*');
		}catch(ex){
		}
	}
}
function regresaWorkspace(){
	try{
		parent.postMessage("regresaWorkspace",'*');
	}catch(ex){
		try{
			window.parent.postMessage("regresaWorkspace",'*');
		}catch(ex){
		}
	}
}
function refrescaFrameWs(){
	try{
		parent.postMessage("refrescaFrameWs",'*');
	}catch(ex){
		try{
			window.parent.postMessage("refrescaFrameWs",'*');
		}catch(ex){
		}
	}
}
function mensajeVolver(){
	try{
		regresa();
	}catch(ex){
	}
	
	try{
		if(esAndroid){				
			$("#btnVolverAndroid").trigger('click');
			$(".btnVolverAndroid").trigger('click');
		}else if(esIos){					
			$("#btnVolverIos").trigger('click');
			$(".btnVolverIos").trigger('click');
		}
		
	}catch(ex){
	}
	
}
//Buzon
var url = 'file.pdf';
var pdfDoc = null,
  pageNum = 1,
  pageRendering = false,
  pageNumPending = null,
  scale = 1.6,
  canvas = null,
  ctx = null,
  divVisorPdr=null,
  divVisorPdrDescarga=null;
  //document.getElementById('the-canvas')
  //canvas.getContext('2d')
var blobBuzon = null;
var xhr = null;
function mainBuzon(){
	var head = document.getElementsByTagName('head')[0]; 

	/*
	//Script 2
	var script2 = document.createElement('script');
	script2.type = 'text/javascript';
	script2.onload = function() {
		//PDFJS.disableWorker = true;
		PDFJS.workerSrc = '/a/js/apps/workspace/buzon/pdf.worker.js';
		//callFunctionFromScript();
	}
	script2.src = '/a/js/apps/workspace/buzon/pdf.js';
	head.appendChild(script2);	
	*/
	
	//creaDivBuzon();
	var u=window.location.href;
	if(u.indexOf("ol-ti-itvisornoti")>=0){			
		cargaListaBuzonPdf();
	}
	if(u.indexOf("cl-ti-iagenerador")>=0){			
		cargaLinksVisor();
	}
}
if(esMovil){
	var u=window.location.href;
	if(u.indexOf("cl-ti-iagenerador")>=0){	
		mainBuzon();  
	}	
}
//mainBuzon();  //*
//oSession.utilReplaceInResponse("var text =","buzonDocumento();var text =");
function buzonDocumento(){	
	//En la primera cargada del buzon esMovil=false; por lo tanto en mainBuzon se carga cargaListaBuzonPdf
	if(esMovil){//*
		cargaListaBuzonPdf();
	}//*
}
function cargaListaBuzonPdf(){
	//var listItems = $(".list-archivo-adjunto li");
	var listItems = $("#listArchivosAdjuntos li");
	listItems.each(function(idx, li) {
		var item = $(li);
		var elementoa=item.children(":first");
		//item.html("<a href=\"javascript:void(0);\" onclick=\"visorPdf('"+elementoa.attr("href")+"');return false;\">"+elementoa.html()+"</div>");
		item.html("<a href=\"javascript:void(0);\" onclick=\"visorPdfDescarga('"+elementoa.attr("href")+"');return false;\">"+elementoa.html()+"</div>");
		
	});
}
function cargaLinksVisor(){
	//var list = document.getElementsByTagName("UL")[0];
	//list.getElementsByTagName("LI")[0].innerHTML = "Test";
	var list = document.getElementsByTagName("a");
	for(var j=0; j<list.length; j++){
		var el=list[j];	
		var hrf=el.href;//JavaScript:goArchivoDescarga(88121,0)
		
		var resId = hrf.substring(hrf.indexOf("(")+1, hrf.indexOf(","));
		var vIdAnexo = hrf.substring(hrf.indexOf(",")+1, hrf.indexOf(")"));
		var arrSistema = vIdAnexo.split(",");
		var resSistema = arrSistema[0];
		
		//alert(resSistema);
		if(resSistema==0){
			try{
				if(typeof window.document.frmArchivo.sistema.value != "undefined"){
					resSistema=window.document.frmArchivo.sistema.value;
				}
			}catch(ex){
			}
		}
		
		var form = window.document.frmArchivo;
		//var link="/ol-ti-itvisornoti/visor/bajarArchivo/"+resId+"/0/"+resSistema;
		var link="/ol-ti-itvisornoti/visor/bajarArchivo?accion=archivo&idMensaje="+form.idMensaje.value+"&idArchivo="+resId+"&sistema="+resSistema+"&app=1";
		//alert(link);
		var st=el.href.toLowerCase();
		if(st.indexOf("javascript:goarchivodescarga")>=0){
			el.setAttribute("href", "javascript:void(0);"); 
			//el.setAttribute("onclick", "visorPdf('"+link+"');return false;"); //antiguo
			el.setAttribute("onclick", "visorPdf2('"+link+"');return false;"); 
			
		}
	}
}
function visorPdf2(url){
	//envia el url al ear del buzon
	try{
		parent.postMessage("frameIniciadoBuzon_"+url,'*');
	}catch(ex){
		try{
			window.parent.postMessage("frameIniciadoBuzon_"+url,'*');
		}catch(ex){
		}
	}
}
function visorPdf(url){
	creaDivBuzon();
	PDFJS.getDocument(url).then(function (pdfDoc_) {
		pdfDoc = pdfDoc_;
		renderPage(pageNum);
	  });
}

function InvokeDownloadManager(url, mimeType){
	if (esAndroid && !(url.indexOf("&app=1")>-1) && mimeType == "application/pdf"){
		try{
			parent.postMessage("frameDownloadManager_" + url,'*');//*
		}catch(ex){
			try{
				window.parent.postMessage("frameDownloadManager_" + url,'*');//*
			}catch(ex){
			}
		}	
		return;
	}else{
		visorPdfDescarga(url);
	}
}

function visorPdfDescarga(url){
	creaDivBuzonDescarga();
	
	var metodo='GET';
	var param='';
	var urlOriginal=url;//+"&nombrePdf=abcd";
	//alert(url.indexOf("app=1"));
	if(url.indexOf("&app=1")>-1){
		metodo='POST';
		url = url.replace("&app=1", "");
		param=url.substring(url.indexOf("?")+1, url.length);
		
		
		url = url.substring(0, url.indexOf("?"));
		//alert('urlpost:'+url);
	}
	
	/////////			
	xhr = new XMLHttpRequest();
	xhr.open(metodo, url, true);
	
	if(metodo=='POST'){
		xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	}

	xhr.responseType = 'blob';

	xhr.onload = function(e) {
	  //alert('1');
	  if (this.status == 200) {
		//alert('2');
		blobBuzon = this.response;
		//Validar tamaño de la descarga
		//alert('blobBuzon.size:'+blobBuzon.size);
		//alert('blobBuzon.type:'+blobBuzon.type);
		
		if(blobBuzon.size>500){
			//manda al workspace
			try{
				parent.postMessage("frameIniciadoBuzonWorkspace_"+urlOriginal,'*');//*
			}catch(ex){
				try{
					window.parent.postMessage("frameIniciadoBuzonWorkspace_"+urlOriginal,'*');//*
				}catch(ex){
				}
			}
			
			//alert(blobBuzon);
			//document.getElementById("myImage").src = window.URL.createObjectURL(blob);
		}else{
			alert('[7.1] Error en la conectividad, tamaño del archivo incorrecto.');
			cierraDivBuzonDescarga();
		}
		
		
	  }else{
		  alert('[1.'+this.status+'] Error en el servidor descargando archivo.');
		  cierraDivBuzonDescarga();
	  }
	};//fin onload
	
	
	
	xhr.onprogress = function(evt) {
		if (evt.lengthComputable){  
			//evt.loaded the bytes browser receive
			//evt.total the total bytes seted by the header
			var percentComplete = (evt.loaded / evt.total)*100;  
			//$('#progressbar').progressbar( "option", "value", percentComplete );
	   } 
	};//fin onprogress
	
	xhr.onabort = function(evt) {
		//alert("Descarga cancelada.");
	};//fin onabort
	
	

	xhr.onerror = function(e) {
	  alert("[2." + e.target.status + "] Error en la conectividad.");
	  cierraDivBuzonDescarga();
	};//fin onerror

	
	if(metodo=='POST'){		
		//alert(param);
		xhr.send(param);
	}else{
		xhr.send();
	}
	
	
	
	/*
	window.requestFileSystem  = window.requestFileSystem || window.webkitRequestFileSystem;

	function onError(e) {
	  alert('Error', e);
	}

	
	alert('1');
	var xhr = new XMLHttpRequest();
	xhr.responseType = 'blob';

	alert('2');
	xhr.onload = function(e) {
		alert('3');
		 if (this.status == 200) {
				window.requestFileSystem(TEMPORARY, 1024 * 1024, function(fs) {
				 //dirName
				fs.root.getDirectory("",
					{create: false, exclusive: false},
					function (dataDir) {
						var fullPath = dataDir.toURL()+"Download/";
						alert("valor dataDir.toURL():" + fullPath);
					},
					function (error) {
						alert("getDirectory error code: " + error.code);
					}); //dirName
				  
				  
				fs.root.getFile('prueba2.pdf', {create: true}, function(fileEntry) {
				  fileEntry.createWriter(function(writer) {

					writer.onwrite = function(e) { alert('ok'); };
					writer.onerror = function(e) { alert('ko'); };

					var blob = new Blob([xhr.response], {type: 'application/pdf'});

					writer.write(blob);

				  }, onError);//createWriter
				}, onError);//getFile
				
				
			  }, onError);//requestFileSystem
		 }//200
		
	  
	};//onload

	xhr.send();*/
	
	/////////
}
function creaDivBuzon(){
	//pdf
	divVisorPdr = document.createElement("div");
	divVisorPdr.setAttribute("id", "divBuzonVisorPdf"); 
	var u=window.location.href;	
	
	divVisorPdr.style.width = "100%";	
	divVisorPdr.style.height = "100%";	
	divVisorPdr.style.minWidth = "100%";	
	divVisorPdr.style.minHeight = "100%";
	
	
	divVisorPdr.style.background = "white";
	divVisorPdr.style.color = "black";
	if(u.indexOf("cl-ti-iagenerador")>=0){	
		divVisorPdr.style.position = "fixed";
	}else{				
		divVisorPdr.style.position = "absolute";
	}
	divVisorPdr.style.left = "0px";
	divVisorPdr.style.top = "0px";
	divVisorPdr.style.zIndex = "999";
	//divVisorPdr.style.display = "none";
	divVisorPdr.style.border = "0px";
	divVisorPdr.style.textAlign = "center";
	divVisorPdr.style.overflow = "auto";
	//divVisorPdr.addEventListener('click', cierraDivBuzon);
	
	//cerrar
	var divBuzonPdfCerrar = document.createElement("div");
	divBuzonPdfCerrar.setAttribute("id", "divBuzonPdfCerrar");
	divBuzonPdfCerrar.innerHTML= "<- Volver";
	divBuzonPdfCerrar.style.fontFamily  ="Arial";
	divBuzonPdfCerrar.style.fontSize ="15px";
	divBuzonPdfCerrar.style.fontWeight  ="bold";
	divBuzonPdfCerrar.style.textAlign  ="center";
	divBuzonPdfCerrar.style.backgroundColor="#CECECE";
	divBuzonPdfCerrar.style.color="#fff";
	divBuzonPdfCerrar.style.position = "fixed";
	divBuzonPdfCerrar.style.right = "5px";
	divBuzonPdfCerrar.style.top = "10px";	
	divBuzonPdfCerrar.style.padding = "10px 0px";	
	divBuzonPdfCerrar.style.width = "80px";
	divBuzonPdfCerrar.style.height = "20px";
	divBuzonPdfCerrar.style.boxSizing = "content-box";	
	divBuzonPdfCerrar.style.borderRadius  = "5px";
	divBuzonPdfCerrar.addEventListener('click', cierraDivBuzon);
	divBuzonPdfCerrar.addEventListener("touchstart", cierraDivBuzon);//ok//*
	divBuzonPdfCerrar.addEventListener("touchcancel", cierraDivBuzon);//ok//*
	divVisorPdr.appendChild(divBuzonPdfCerrar);
	
	
	//spinner	
	var imgSpinner = document.createElement("img");
	imgSpinner.src = "/a/imagenes/wait-big.gif";
	imgSpinner.style.display = "none";
	
	//divVisorPdr.appendChild(imgSpinner);
	
	//alert(divVisorPdr.id);
	
	canvas = document.createElement("canvas");
	canvas.style.width = "100%";
	canvas.style.height = "100%";
	canvas.style.border = "0px";
	canvas.style.background="url(/a/imagenes/wait-big.gif) center center no-repeat";
	//canvas.addEventListener('click', cierraDivBuzon);//*
	
	//canvas.addEventListener("touchstart", cierraDivBuzon);//ok//*
	//canvas.addEventListener("touchend", function(){alert('2');}, false);
	//canvas.addEventListener("touchcancel", cierraDivBuzon);//ok//*
	//canvas.addEventListener("touchleave", function(){alert('4');}, false);
	//canvas.addEventListener("touchmove", function(){alert('5');}, false);
		
	ctx = canvas.getContext('2d');
	divVisorPdr.appendChild(canvas);
	document.body.appendChild(divVisorPdr);
}
function creaDivBuzonDescarga(){
	//pdf descarga
	divVisorPdrDescarga = document.createElement("div");
	divVisorPdrDescarga.setAttribute("id", "divBuzonVisorPdfDescarga"); 
	var u=window.location.href;	
	
	divVisorPdrDescarga.style.width = "100%";	
	divVisorPdrDescarga.style.height = "100%";	
	divVisorPdrDescarga.style.minWidth = "100%";	
	divVisorPdrDescarga.style.minHeight = "100%";
	
	
	divVisorPdrDescarga.style.background = "white";
	divVisorPdrDescarga.style.color = "black";
	if(u.indexOf("cl-ti-iagenerador")>=0){	
		divVisorPdrDescarga.style.position = "fixed";
	}else{				
		divVisorPdrDescarga.style.position = "absolute";
	}
	divVisorPdrDescarga.style.left = "0px";
	divVisorPdrDescarga.style.top = "0px";
	divVisorPdrDescarga.style.zIndex = "999";
	//divVisorPdrDescarga.style.display = "none";
	divVisorPdrDescarga.style.border = "0px";
	divVisorPdrDescarga.style.textAlign = "center";
	divVisorPdrDescarga.style.overflow = "auto";
	//divVisorPdrDescarga.addEventListener('click', cierraDivBuzonDescarga);
	
	//cerrar
	var divBuzonPdfCerrar = document.createElement("div");
	divBuzonPdfCerrar.setAttribute("id", "divBuzonPdfCerrar");
	divBuzonPdfCerrar.innerHTML= "Cancelar";
	divBuzonPdfCerrar.style.fontFamily  ="Arial";
	divBuzonPdfCerrar.style.fontSize ="15px";
	divBuzonPdfCerrar.style.fontWeight  ="bold";
	divBuzonPdfCerrar.style.textAlign  ="center";
	divBuzonPdfCerrar.style.backgroundColor="#CECECE";
	divBuzonPdfCerrar.style.color="#fff";
	divBuzonPdfCerrar.style.position = "fixed";
	divBuzonPdfCerrar.style.right = "5px";
	divBuzonPdfCerrar.style.top = "10px";	
	divBuzonPdfCerrar.style.padding = "10px 0px";	
	divBuzonPdfCerrar.style.width = "80px";
	divBuzonPdfCerrar.style.height = "20px";
	divBuzonPdfCerrar.style.boxSizing = "content-box";	
	divBuzonPdfCerrar.style.borderRadius  = "5px";
	divBuzonPdfCerrar.addEventListener('click', cierraDivBuzonDescarga);
	divBuzonPdfCerrar.addEventListener("touchstart", cierraDivBuzonDescarga);//ok//*
	divBuzonPdfCerrar.addEventListener("touchcancel", cierraDivBuzonDescarga);//ok//*
	divVisorPdrDescarga.appendChild(divBuzonPdfCerrar);
	
	
	//spinner	
	var imgSpinner = document.createElement("img");
	imgSpinner.src = "/a/imagenes/wait-big.gif";
	imgSpinner.style.display = "none";
	
	//divVisorPdrDescarga.appendChild(imgSpinner);
	
	//alert(divVisorPdrDescarga.id);
	
	
	canvas = document.createElement("canvas");
	canvas.style.width = "100%";
	canvas.style.height = "100%";
	canvas.style.border = "0px";
	canvas.style.background="url(/a/imagenes/wait-big.gif) center center no-repeat";
	
	//canvas.addEventListener('click', cierraDivBuzonDescarga);//*
	
	//canvas.addEventListener("touchstart", cierraDivBuzonDescarga);//ok//*
	//canvas.addEventListener("touchend", function(){alert('2');}, false);
	//canvas.addEventListener("touchcancel", cierraDivBuzonDescarga);//ok//*
	//canvas.addEventListener("touchleave", function(){alert('4');}, false);
	//canvas.addEventListener("touchmove", function(){alert('5');}, false);
		
		
	ctx = canvas.getContext('2d');
	divVisorPdrDescarga.appendChild(canvas);
	document.body.appendChild(divVisorPdrDescarga);
}
function cierraDivBuzon(){
	try{
		//alert(divVisorPdr.id);
		//divVisorPdr.style.display = "none";
		document.body.removeChild(document.getElementById("divBuzonVisorPdf"));
		//document.getElementById("divBuzonVisorPdf").display = "none";
	}catch(err) {		
	}
}

function cierraDivBuzonDescarga(){
	try{
		//alert(divVisorPdrDescarga.id);
		//divVisorPdrDescarga.style.display = "none";
		//TODO: cancelar descarga
		document.body.removeChild(document.getElementById("divBuzonVisorPdfDescarga"));
		
		try{
			xhr.abort();		
		}catch(err) {		
		}
		//document.getElementById("divBuzonVisorPdfDescarga").display = "none";
	}catch(err) {		
	}
}
function renderPage(num) {
    pageRendering = true;
    // Using promise to fetch the page
    pdfDoc.getPage(num).then(function(page) {
      var viewport = page.getViewport(scale);//scale
	  
      canvas.style.height = viewport.height+"px";
      canvas.style.width = viewport.width+"px";
      canvas.height = viewport.height;
      canvas.width = viewport.width;

      // Render PDF page into canvas context
      var renderContext = {
        canvasContext: ctx,
        viewport: viewport
      };
      var renderTask = page.render(renderContext);

      // Wait for rendering to finish
      renderTask.promise.then(function () {
        pageRendering = false;
        if (pageNumPending !== null) {
          // New page rendering is pending
          renderPage(pageNumPending);
          pageNumPending = null;
        }
      });//fin renderTask.promise.then
	  
	  
    });//fin getPage

    // Update page counters
    //document.getElementById('page_num').textContent = pageNum;
  }

  function queueRenderPage(num) {
    if (pageRendering) {
      pageNumPending = num;
    } else {
      renderPage(num);
    }
  }

  function onPrevPage() {
    if (pageNum <= 1) {
      return;
    }
    pageNum--;
    queueRenderPage(pageNum);
  }

  function onNextPage() {
    if (pageNum >= pdfDoc.numPages) {
      return;
    }
    pageNum++;
    queueRenderPage(pageNum);
  }
  

//Recibos por honorarios   
if(u.indexOf("cl-ti-iagenerador")>=0){			
}else{
	$("#btnNuevaConsultaRhe").bind('click',function(event){
		var href = $("#aNuevaConsultaRhe").attr('href');
		window.location.href = href;
		
		
		event.preventDefault();
		event.stopImmediatePropagation();
		return false;
	}); 
}

function irHomeRhe(){
	$("#btnNuevaConsultaRhe").trigger('click');
}



//Factura Movil
if(u.indexOf("cl-ti-iagenerador")>=0){			
}else{
	$("#btnNuevaConsultaFactura").bind('click',function(event){
		var href = $("#aNuevaConsultaFactura").attr('href');
		window.location.href = href;
		
		
		event.preventDefault();
		event.stopImmediatePropagation();
		return false;
	}); 
}
   


function irHomeFactura(){
	$("#btnNuevaConsultaFactura").trigger('click');
}

/*
divSignonFormLogo
divSignonFormFooter
divSignonFormCandado
aOlvidaste

h1{
	font-size: 1.7em;
}
.header div{
	padding-left: 0 !important;
} 
.imgLogo{
	height: 2.5em;
	margin-top: 1em;
}
.blockUI h1{
	font-size: 12px !important;
}
*/
/*Fin funciones móvil*/

function APPMovil_goArchivoDescarga(idArchivo, idAnexo, indicadorMsg) {
	
	if (indicadorMsg == undefined) indicadorMsg = "5";
	
	
	if(esAndroid){
		try{
			Android.goArchivoDescarga(idArchivo, indicadorMsg);
		}catch(ex){
			alert(ex);
		}
	}
	else if(esIos){
	   try {
			var datos = {idArchivo: idArchivo, indicadorMsg: indicadorMsg};
			window.webkit.messageHandlers.goArchivoDescarga.postMessage(datos);
	   } catch(err) {
		   alert("goArchivoDescarga() " + err);
	   }
	}
}

function APPMovil_goPagoValores() {
    if(esAndroid){
		Android.goPagoValores();
	}
	else if(esIos){
	   try {
			window.webkit.messageHandlers.goPagoValores.postMessage("");
	   } catch(err) {
		   alert("goPagoValores() " + err);
	   }
	}
}
/*FIN - FUNCIONES APP BUZON*/
