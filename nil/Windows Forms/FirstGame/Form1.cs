using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Game
{
   
    public partial class Form1 : Form
    {
        private Point point;
        private bool dragging;
        public Form1()
        {
            InitializeComponent();
            Phon1.MouseDown += MouseClickDown;
            Phon1.MouseUp += MouseClickUp;
            Phon1.MouseMove += MouseClickMove;
            Phon2.MouseDown += MouseClickDown;
            Phon2.MouseUp += MouseClickUp;
            Phon2.MouseMove += MouseClickMove;
        }

        private void Form1_KeyPress(object sender, KeyPressEventArgs e)
        {
            
            if (e.KeyChar == (char)Keys.Escape)
            {
                this.Close();
            }
            

        }
        private void MouseClickDown(object sender, MouseEventArgs e)
        {
            dragging = true;
            point.X = e.X;
            point.Y = e.Y;
        }
        private void MouseClickUp(object sender, MouseEventArgs e)
        {
            dragging = false;
        }
        private void MouseClickMove(object sender, MouseEventArgs e)
        {
            if (dragging)
            {
                Point pos = PointToScreen(new Point(e.X, e.Y));
                this.Location = new Point(pos.X - point.X, pos.Y - point.Y + Phon1.Top);
            }
        }
        private void timer1_Tick(object sender, EventArgs e)
        {
            int speed = 5;
            Phon1.Top += speed;
            Phon2.Top += speed;
            int carSpeed = 10;
            Sop1.Top += carSpeed;
            Sop2.Top += carSpeed;
            if (Phon1.Top >= 600)
            {
                Phon1.Top = 0;
                Phon2.Top = -600;

            }
            if (Sop1.Top >= 600) 
            { 
                Sop1.Top = -200;
                Random random = new Random();
                Sop1.Left = random.Next(180,330);
            }
            if (Sop2.Top >= 600)
            {
                Sop2.Top = -400;
                Random random = new Random();
                Sop2.Left = random.Next(420,580);
            }
            if (Car.Bounds.IntersectsWith(Sop1.Bounds) || Car.Bounds.IntersectsWith(Sop2.Bounds))
            {
                timer.Enabled = false;
                MessageBox.Show("Вы проиграли");
                this.Close();
            }
            
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            int speed = 10;
            if((e.KeyCode == Keys.A || e.KeyCode == Keys.Left) && Car.Left > 165)
            {
                Car.Left -= speed;
            }
            if((e.KeyCode == Keys.D || e.KeyCode == Keys.Right) && Car.Right < 675)
            {
                Car.Left += speed;
            }
            if((e.KeyCode == Keys.W || e.KeyCode == Keys.Up) && Car.Top > 150)
            {
                Car.Top -= speed;
            }
            if((e.KeyCode == Keys.S || e.KeyCode == Keys.Down) && Car.Top < 450)
            {
                Car.Top += speed;
            }
        }
    }
}
