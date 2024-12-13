import pyautogui as auto
import time

# Teks kode yang ingin Anda ketik
kode = """
import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class JTableExample {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Form Tabel dengan Input Pengguna");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 400);
        frame.setLayout(new BorderLayout());

        String[][] data = {
            {"1", "Budi", "Santoso", "25"},
            {"2", "Siti", "Nurhaliza", "30"},
            {"3", "Ahmad", "Suhendra", "40"},
            {"4", "Dewi", "Putri", "35"}
        };
        String[] columns = {"ID", "Nama Depan", "Nama Belakang", "Usia"};

        DefaultTableModel model = new DefaultTableModel(data, columns);
        JTable table = new JTable(model);
        JScrollPane scrollPane = new JScrollPane(table);
        frame.add(scrollPane, BorderLayout.CENTER);

        JPanel panel = new JPanel();
        panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));

        JTextField idField = new JTextField(20);
        JTextField namaDepanField = new JTextField(20);
        JTextField namaBelakangField = new JTextField(20);
        JTextField usiaField = new JTextField(20);

        panel.add(new JLabel("ID:"));
        panel.add(idField);
        panel.add(new JLabel("Nama Depan:"));
        panel.add(namaDepanField);
        panel.add(new JLabel("Nama Belakang:"));
        panel.add(namaBelakangField);
        panel.add(new JLabel("Usia:"));
        panel.add(usiaField);

        JButton addButton = new JButton("Tambah Data");
        panel.add(addButton);
        frame.add(panel, BorderLayout.NORTH);

        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String id = idField.getText();
                String namaDepan = namaDepanField.getText();
                String namaBelakang = namaBelakangField.getText();
                String usia = usiaField.getText();

                model.addRow(new Object[]{id, namaDepan, namaBelakang, usia});

                idField.setText("");
                namaDepanField.setText("");
                namaBelakangField.setText("");
                usiaField.setText("");
            }
        });

        frame.setVisible(true);
    }
}
"""

# Tunggu beberapa detik agar Anda bisa memfokuskan editor
print("Tunggu 5 detik untuk memfokuskan jendela editor kode...")
time.sleep(5)

# Mengetikkan kode dalam editor
for char in kode:
    auto.typewrite(char)
    time.sleep(0.05)  # Jeda antara karakter, sesuaikan kecepatannya
