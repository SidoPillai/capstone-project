import java.io.BufferedOutputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class ConnectionReceiver extends Thread {

	ServerSocket ss;

	private final static int PORT = 2500;

	public void run() {
		try {
			ss = new ServerSocket(PORT);

			while(true) {
				new HandleRequest(ss.accept()).start();
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	private class HandleRequest extends Thread {

		private Socket socket;
		private InputStream is;
		public final static String FILE_TO_RECEIVED = "/Users/siddeshpillai/Desktop/blah/images/image.png";
		FileOutputStream fos = null;
		BufferedOutputStream bos = null;
		public final static int FILE_SIZE = 6022386;

		public HandleRequest(Socket clientSocketConnection) {
			this.socket = clientSocketConnection;

			try {
				is = socket.getInputStream();
				fos = new FileOutputStream(FILE_TO_RECEIVED);
				bos = new BufferedOutputStream(fos);
			} catch (IOException e) {
				e.printStackTrace();
			}
		}

		public void run() {
			int bytesRead;
			int current = 0;
			try {

				// receive file
				byte [] mybytearray  = new byte [FILE_SIZE];
				bytesRead = is.read(mybytearray,0,mybytearray.length);
				current = bytesRead;

				do {
					bytesRead =
							is.read(mybytearray, current, (mybytearray.length-current));
					if(bytesRead >= 0) current += bytesRead;
				} while(bytesRead > -1);

				bos.write(mybytearray, 0 , current);
				bos.flush();
				System.out.println("File " + FILE_TO_RECEIVED
						+ " downloaded (" + current + " bytes read)");
				
				fos.close();
				bos.close();
				
			} catch(Exception e) {
				System.out.println(e.getMessage());
			}
		}
	}

}
