
#include <graphics.h>
#include <stdlib.h>
#include <stdio.h>
#include <conio.h>
void dda(float,float,float,float);
void main(void)
{
   int gd=DETECT,gm;
   int x1,x2,y1,y2;
   clrscr();
   printf(" enter x1,y1,x2,y2 \n");
   scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
   initgraph(&gd, &gm, "C:\\TURBOC3\\BGI");
   dda(x1,y1,x2,y2);
   getch();
   closegraph();
}
   void dda(float x1,float y1, float x2, float y2)
   {
    int gd=DETECT,gm;
    float dx,dy,m,x_inc=0.0,y_inc=0.0;//m is slope
    int step=0,i;

   dx=x2-x1;
   dy=y2-y1;


   cleardevice();
   if (abs(dx)>abs(dy))
   {
	step=abs(dx);
   }
   else
   {
	step=abs(dy) ;
   }
   x_inc=dx/step;
   y_inc=dy/step;
   for(i=1;i<step;i++)
   {
	putpixel(x1,y1,GREEN);
	x1=x1+ x_inc;
	y1=y1+y_inc;
}
}