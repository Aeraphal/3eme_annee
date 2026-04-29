#version 330 core

// Variable de sortie (sera utilisé comme couleur)
out vec4 color;

//Un Fragment Shader minimaliste
uniform vec4 couleur;
void main (void)
{
  float x=gl_FragCoord.x/800.0-0.5;
  float y=gl_FragCoord.y/800.0-0.5;
  color = vec4(1.0,0.1,0.0,0.0);
}


//if(x*x + y*y>0.2*0.5)
//  color = vec4(0.0,1.0,0.0,1.0);
//else
//  color = vec4(1.0,0.0,0.0,1.0);