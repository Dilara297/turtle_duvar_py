import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class DuvardanKacan(Node):
    def __init__(self):
        super().__init__('duvardan_kacan')

        # Bonus: Hız ve sınır değerleri parametreleri
        self.declare_parameter('speed', 2.0)
        self.declare_parameter('limit_alt', 1.0)
        self.declare_parameter('limit_ust', 10.0)

        # Yayıncı ve Abone tanımlamaları
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscriber_ = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)

        # Log için saniyede bir çalışan timer
        self.log_timer = self.create_timer(1.0, self.log_callback)

        self.current_pose = Pose()

    def pose_callback(self, msg):
        self.current_pose = msg
        
        # Parametreleri güncel olarak çek
        speed = self.get_parameter('speed').value
        limit_alt = self.get_parameter('limit_alt').value
        limit_ust = self.get_parameter('limit_ust').value

        cmd = Twist()

        # Konum x veya y 1.0'dan küçük ya da 10.0'dan büyükse dönüş yap
        if (msg.x < limit_alt or msg.x > limit_ust or 
            msg.y < limit_alt or msg.y > limit_ust):
            cmd.linear.x = speed  # Dönüş anında dışarı savrulmamak için hızı düşür
            cmd.angular.z = 2.5         # Dönerek yön değiştir
        else:
            cmd.linear.x = speed        # Güvenli alanda ileri sür[cite: 1]
            cmd.angular.z = 0.0

        self.publisher_.publish(cmd)

    def log_callback(self):
        # Konumu saniyede bir info seviyesinde yazdır[cite: 1]
        self.get_logger().info(f'Konum -> X: {self.current_pose.x:.2f}, Y: {self.current_pose.y:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = DuvardanKacan()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
