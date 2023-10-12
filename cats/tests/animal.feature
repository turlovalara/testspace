Feature: Animal


  @regression
  Scenario: Dog say
    # Генерация животного
    Given birth of a "dog" and call "Bob"
    # Животное говорит
    When "Bob" says save it as "said"
    # Проверить, что сказало животное
    Then assert animal said "Gav!"


  @regression
  Scenario: Cat say
    # Генерация животного
    Given birth of a "cat" and call "Vasya"
    # Животное говорит
    When "Vasya" says save it as "said"
    # Проверить, что сказало животное
    Then assert animal said "Meow!"
