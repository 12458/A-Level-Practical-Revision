import socket
gp_grade = input("GP Grade:")
pw_grade = input("PW Grade:")
H2_1_grade = input("1st H2 subject grade:")
H2_2_grade = input("2nd H2 subject grade:")
H2_3_grade = input("3rd H2 subject grade:")
H1_grade = input("H1 Grade/Lowest H2 subject grade:")
s = socket.socket()
s.connect(("127.0.0.1",9999))
s.sendall( f"{gp_grade},{pw_grade},{H2_1_grade},{H2_2_grade},{H2_3_grade},{H1_grade}".encode() +
b"\n")
UAS = s.recv(1024)
print(f"UAS:{UAS.decode()}")
s.close()
