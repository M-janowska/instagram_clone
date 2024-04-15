import {
  Box,
  Button,
  Image,
  Input,
  VStack,
  Text,
  Flex,
} from "@chakra-ui/react";
import { useState } from "react";

const AuthForm = () => {
  const [isLogin] = useState(true);
  return (
    <>
      <Box border={"1px solid gray"} borderRadius={4} padding={5}>
        <VStack spacing={4}>
          <Image src="/logo.png" h={24} cursor={"pointer"} alt="Instagram" />

          <Input placeholder="Email" fontsize={14} type="email" />

          <Input placeholder="Password" fontsize={14} type="password" />

          {!isLogin ? (
            <Input
              placeholder="Confirm password"
              fontsize={14}
              type="password"
            />
          ) : null}

          <Button w={"full"} colorScheme="blue" size={"sm"} fontsize={14}>
            {isLogin ? "Login" : "Sign up"}
          </Button>

          <Flex
            alignItems={"center"}
            justifyContent={"center"}
            my={"4"}
            gap={"1"}
            w={"full"}
          >
            <Box flex={2} h={"1px"} bg={"gray.400"} />
            <Text mx={1} color={"white"}>
              OR
            </Text>
            <Box flex={2} h={"1px"} bg={"gray.400"} />
          </Flex>
        </VStack>
      </Box>
    </>
  );
};

export default AuthForm;
