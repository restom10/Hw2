#include <cmath>
#include <iostream>
#include <fstream>


using namespace std; 

int main()
{
    double m1=1000;
    double m2=1000;
    double m3=1000;
    
    double k=2000;
    
    double w=sqrt(k/m1);
    cout<<w;
    //Condiciones iniciales 
    double v1[100];
    double v2[100];
    double v3[100];
    
    double u1[100];
    double u2[100];
    double u3[100];
    
    v1[0]=0;
    v2[0]=0;
    v3[0]=0;
    
    u1[0]=0;
    u2[0]=0;
    u3[0]=0;
    
    double d=0.15;
    
    //Varios w
    
    double delta=(3-0.2)/100;
    double ws[100];
    double cons=0.2;
    ws[0]=cons*w;
    
    for(int i=1;i<=99;i++)
    {
        cons+=delta;
        ws[i]=(cons)*w;
    }
    
    
    double maxsU1[100];
    double maxsU2[100];
    double maxsU3[100];
    
    for(int i=0;i<=72;i++)
    {
    double a=ws[i]*ws[i];        
    for(int t=1;t<=72;t++)
    {
        v1[t]=v1[t-1]+d*(-2*a*u1[t-1]+a*u2[t-1]+sin(ws[i]*t)/m1);
        v2[t]=v2[t-1]+d*(a*u1[t-1]-2*a*u2[t-1]+a*u3[t-1]);
        v3[t]=v3[t-1]+d*(a*u2[t-1]-a*u3[t-1]);
        
        u1[t]=u1[t-1]+d*v1[t-1];
        u2[t]=u2[t-1]+d*v2[t-1];
        u3[t]=u3[t-1]+d*v3[t-1];
    
    }
              
    double maxU1=0;
    for(int i=0;i<=72;i++)
    {
    
        if(u1[i]>=maxU1)
        {
            maxU1=u1[i];
        }
    
    }
    
    maxsU1[i]=maxU1;
    
    double maxU2=0;
    for(int i=0;i<=72;i++)
    {
    
        if(u2[i]>=maxU2)
        {
            maxU2=u2[i];
        }
    
    }
 
    maxsU2[i]=maxU2;
        
        
    double maxU3=0;
    for(int i=0;i<=72;i++)
    {
    
        if(u3[i]>=maxU3)
        {
            maxU3=u3[i];
        }
    
    }
    maxsU3[i]=maxU3;
              
    }
    
    
    ofstream outfile;
    outfile.open("U1.txt");
    for(int i=0;i<=72;i++)
    {
        outfile << ws[i]<<';'<<maxsU1[i]<<"\n";
    }
    
    outfile.close();
    
 
    outfile.open("U2.txt");
    for(int i=0;i<=72;i++)
    {
        outfile << ws[i]<<';'<<maxsU2[i]<<"\n";
    }
    
    outfile.close();


    outfile.open("U3.txt");
    for(int i=0;i<=72;i++)
    {
        outfile << ws[i]<<';'<<maxsU3[i]<<"\n";
    }
    
    outfile.close();





    return 0; 
}