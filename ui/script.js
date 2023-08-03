// Obtén una referencia al elemento en el que deseas agregar los enlaces
const socialMediaContainer = document.getElementById('social-media-content');

// Datos de las redes sociales (esto podría provenir de tus APIs)
const socialMediaLinks = [
  { name: 'Facebook', url: 'https://www.facebook.com' },
  { name: 'Twitter', url: 'https://www.twitter.com' },
  { name: 'Instagram', url: 'https://www.instagram.com' },
  // Agrega más redes sociales según tus necesidades
];

// Recorre los datos y crea enlaces para cada red social
socialMediaLinks.forEach(socialMedia => {
  const link = document.createElement('a');
  link.href = socialMedia.url;
  link.textContent = socialMedia.name;
  link.target = '_blank'; // Abre en una nueva pestaña

  socialMediaContainer.appendChild(link);
});
