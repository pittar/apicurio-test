openapi: 3.0.2
info:
    title: countries
    version: 1.0.0
    description: A brand new API with no content.  Go nuts!
paths:
    /countries:
        summary: Path used to manage the list of countries.
        description: >-
            The REST endpoint/path used to list and create zero or more `country` entities.  This path
            contains a `GET` and `POST` operation to perform the list and create tasks, respectively.
        get:
            responses:
                '200':
                    content:
                        application/json:
                            schema:
                                type: array
                                items:
                                    $ref: '#/components/schemas/country'
                            examples:
                                countries:
                                    value:
                                        -
                                            name: Spain
                                            currency: EUR
                                            capital: Madrid
                                        -
                                            name: United Kingdom
                                            currency: GBP
                                            capital: London
                    description: Successful response - returns an array of `country` entities.
            operationId: getcountries
            summary: List All countries
            description: Gets a list of all `country` entities.
        post:
            requestBody:
                description: A new `country` to be created.
                content:
                    application/json:
                        schema:
                            $ref: '#/components/schemas/country'
                required: true
            responses:
                '201':
                    description: Successful response.
            operationId: createcountry
            summary: Create a country
            description: Creates a new instance of a `country`.
    '/countries/{countryId}':
        summary: Path used to manage a single country.
        description: >-
            The REST endpoint/path used to get, update, and delete single instances of an `country`.  This
            path contains `GET`, `PUT`, and `DELETE` operations used to perform the get, update, and delete
            tasks, respectively.
        get:
            parameters:
                -
                    examples:
                        countryid:
                            value: Spain
                    name: countryId
                    description: A unique identifier for a `country`.
                    schema:
                        type: string
                    in: path
                    required: true
            responses:
                '200':
                    content:
                        application/json:
                            schema:
                                $ref: '#/components/schemas/country'
                            examples:
                                acountry:
                                    value:
                                        name: Spain
                                        currency: EUR
                                        capital: Madrid
                    description: Successful response - returns a single `country`.
            operationId: getcountry
            summary: Get a country
            description: Gets the details of a single instance of a `country`.
        put:
            requestBody:
                description: Updated `country` information.
                content:
                    application/json:
                        schema:
                            $ref: '#/components/schemas/country'
                required: true
            responses:
                '202':
                    description: Successful response.
            operationId: updatecountry
            summary: Update a country
            description: Updates an existing `country`.
        delete:
            responses:
                '204':
                    description: Successful response.
            operationId: deletecountry
            summary: Delete a country
            description: Deletes an existing `country`.
        parameters:
            -
                name: countryId
                description: A unique identifier for a `country`.
                schema:
                    type: string
                in: path
                required: true
components:
    schemas:
        country:
            description: Country Info.
            required:
                - name
                - currency
                - capital
            type: object
            properties:
                name:
                    description: Country name.
                    type: string
                currency:
                    description: Country currency code.
                    type: string
                capital:
                    description: Capital city.
                    type: string
    responses:
        country:
            content:
                application/json:
                    schema:
                        $ref: '#/components/schemas/country'
                    examples:
                        countryspain:
                            value:
                                name: Spain
                                currency: EUR
                                capital: Madrid
            description: A country info response.

