class Service:
    def __init__(self):
        self.is_running = False
        self.config = {}

    def start(self):
        """Запуск сервиса"""
        if not self.is_running:
            self.is_running = True
            print("Сервис запущен")
            self._initialize()
        else:
            print("Сервис уже запущен")

    def stop(self):
        """Остановка сервиса"""
        if self.is_running:
            self.is_running = False
            print("Сервис остановлен")
            self._cleanup()
        else:
            print("Сервис не запущен")

    def configure(self, config: dict):
        """Настройка сервиса с предоставленными параметрами"""
        self.config.update(config)
        print("Сервис настроен с новыми параметрами")

    def _initialize(self):
        """Внутренний метод для инициализации ресурсов сервиса"""
        # Инициализация ресурсов, соединений и т.д.
        pass

    def _cleanup(self):
        """Внутренний метод для очистки ресурсов сервиса"""
        # Очистка ресурсов, закрытие соединений и т.д.
        pass


# Пример использования
if __name__ == "__main__":
    # Создаем экземпляр сервиса
    my_service = Service()

    # Настраиваем сервис
    my_service.configure({
        "host": "localhost",
        "port": 8080,
        "timeout": 30
    })

    # Запускаем сервис
    my_service.start()

    # Здесь выполняется основная работа

    # Останавливаем сервис
    my_service.stop()
    #my_server
