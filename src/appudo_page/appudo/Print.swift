/*
    Print.swift is part of Appudo

    Copyright (C) 2015-2016
        4bea15c834854bf9670dc6a1cbc9a9dda7cf418ef53b8edbb11b3df946a0c45e source@appudo.com

    Licensed under the Apache License, Version 2.0

    See http://www.apache.org/licenses/LICENSE-2.0 for more information
*/

import libappudo_bridge


public struct OutDummy
{
}

public let out : OutDummy = OutDummy()

/**
Print to output without a newline.
*/
public func << (_ out : OutDummy, _ value : Any) -> OutDummy {
    print(value, terminator:"")
    return out
}
