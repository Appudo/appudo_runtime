/*
    HTTPRequestType.swift is part of Appudo

    Copyright (C) 2015-2016
        4bea15c834854bf9670dc6a1cbc9a9dda7cf418ef53b8edbb11b3df946a0c45e source@appudo.com

    Licensed under the Apache License, Version 2.0

    See http://www.apache.org/licenses/LICENSE-2.0 for more information
*/

/**
HTTPRequestType contains the type of a http request.

- SeeAlso: HTTPClient
*/
public enum HTTPRequestType : Int {
    case GET = 0
    case POST = 1
    case DELETE = 2
    case PUT = 3
}
