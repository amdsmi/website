from service import Service


def main():
    service = None

    try:
        service = Service()

        print('Running API Gateway Service...')
        service.run()

        service.join()

    finally:
        if service is not None and service.is_running:
            print('Stopping API Gateway Service...')
            service.stop()


if __name__ == '__main__':
    main()