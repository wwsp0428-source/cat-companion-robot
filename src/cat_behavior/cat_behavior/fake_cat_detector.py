import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class FakeCatDetector(Node):
    def __init__(self):
        super().__init__('fake_cat_detector')

        self.publisher_ = self.create_publisher(
            String,
            '/cat_direction',
            10
        )

        self.timer = self.create_timer(1.0, self.timer_callback)

        self.directions = ['left', 'center', 'right']
        self.index = 0

    def timer_callback(self):
        msg = String()
        msg.data = self.directions[self.index]

        self.publisher_.publish(msg)

        self.get_logger().info(
            f'Cat direction: {msg.data}'
        )

        self.index = (self.index + 1) % len(self.directions)


def main(args=None):
    rclpy.init(args=args)

    node = FakeCatDetector()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
