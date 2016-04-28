import java.io.DataOutputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.net.Socket;
import java.net.UnknownHostException;

public class Client {
	
	private static Socket clientSocket;
	
	public static void main(String[] args) throws UnknownHostException, IOException {
		
		clientSocket = new Socket("192.168.1.13", 2500);
		System.out.println("Connecting to....");
		sendFile("query.png");
	}

	public static void sendFile(String file) throws IOException {
		DataOutputStream dos = new DataOutputStream(clientSocket.getOutputStream());
		FileInputStream fis = new FileInputStream(file);
		byte[] buffer = new byte[4096];

		while (fis.read(buffer) > 0) {
			dos.write(buffer);
		}

		fis.close();
		dos.close();	
	}

}
