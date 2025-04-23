using System.Diagnostics;

namespace Zotepad_Installer
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void InstallReplace()
        {
                System.IO.File.Move("C:\\Windows\\System32\\notepad.exe", "C:\\Windows\\System32\\notepad1.exe");
                File.Copy(@"notepad.exe", @"C:\Windows\System32\notepad.exe", true);
                MessageBox.Show("Завешерно!");
        }

        private void guna2Button2_Click(object sender, EventArgs e)
        {
                File.Delete("C:\\Windows\\System32\\notepad.exe");
                System.IO.File.Move("C:\\Windows\\System32\\notepad1.exe", "C:\\Windows\\System32\\notepad.exe");
                MessageBox.Show("Завешерно!");
        }

        private void guna2Button1_Click(object sender, EventArgs e)
        {
            InstallReplace();
        }

        private void guna2PictureBox1_Click(object sender, EventArgs e)
        {

        }

        private void guna2Button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void guna2Button4_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;
        }

        private void guna2HtmlLabel1_Click(object sender, EventArgs e)
        {
            Process.Start(new ProcessStartInfo("https://t.me/kARTEL_EZZtemp") { UseShellExecute = true });
        }

        private void label2_Click(object sender, EventArgs e)
        {
            Process.Start(new ProcessStartInfo("https://github.com/mansar1337") { UseShellExecute = true });
        }

        private void label4_Click(object sender, EventArgs e)
        {
            Process.Start(new ProcessStartInfo("https://github.com/EzzTEMP") { UseShellExecute = true });
        }
    }
}
