# Please navigate to original feature_extractors.py and add this to the importing libraries section
from metavision_core_ml.core.modules import ConvLayer,ResBlock,Bottleneck
from metavision_core_ml.core.modules import PreActBlock

# Please, add this to the end of the original code
class Resnet_18(nn.Module):

    def __init__(self, cin=1, base=16, cout=256):
        print('ResNet-18')
        super(Resnet_18, self).__init__()
        self.base = base
        self.cout = cout
        self.levels = 5

        self.conv1 = SequenceWise(nn.Sequential(
            ConvLayer(cin, self.base, kernel_size=7, stride=2, padding=3),
            nn.MaxPool2d(kernel_size=3,stride=2,padding=1),
            ResBlock(base,16,1),
            ResBlock(16,16,1),
            ResBlock(16,32,1),
            ResBlock(32,32,1),
            ResBlock(32,64,1),
            ResBlock(64,64,1),
            ResBlock(64,128,1),
            ResBlock(128,128,1)
        

        ))
        self.conv2 = nn.ModuleList()
        self.conv2.append(ConvRNN(self.base * 8, cout, stride=2))
        for i in range(4):
            self.conv2.append(ConvRNN(self.cout, self.cout, stride=2))

    def forward(self, x):
        x = self.conv1(x)
        output = []
        for conv in self.conv2:
            x = conv(x)
            y = time_to_batch(x)[0]
            output.append(y)
        return output

    def reset(self, mask=None):
        for name, module in self.conv2.named_modules():
            if hasattr(module, "reset"):
                module.reset(mask)

    @torch.jit.export
    def reset_all(self):
        for module in self.conv2:
            module.reset_all()



class ResNet_34(nn.Module):

    print('ResNet-34')
    def __init__(self, cin=1, base=16, cout=256):
        super(ResNet_34, self).__init__()
        self.base = base
        self.cout = cout
        self.levels = 5

        self.conv1 = SequenceWise(nn.Sequential(
            ConvLayer(cin, self.base, kernel_size=7, stride=2, padding=3),
            nn.MaxPool2d(kernel_size=3,stride=2,padding=1),
            ResBlock(base,16,1),
            ResBlock(16,16,1),
            ResBlock(16,16,1),
            ResBlock(16,32,1),
            ResBlock(32,32,1),
            ResBlock(32,32,1),
            ResBlock(32,32,1),
            ResBlock(32,64,1),
            ResBlock(64,64,1),
            ResBlock(64,64,1),
            ResBlock(64,64,1),
            ResBlock(64,64,1),
            ResBlock(64,64,1),
            ResBlock(64,128,1),
            ResBlock(128,128,1),
            ResBlock(128,128,1)
        

        ))
        self.conv2 = nn.ModuleList()
        self.conv2.append(ConvRNN(self.base * 8, self.cout, stride=2))
        for i in range(4):
            self.conv2.append(ConvRNN(cout, cout, stride=2))

    def forward(self, x):
        x = self.conv1(x)
        output = []
        for conv in self.conv2:
            x = conv(x)
            y = time_to_batch(x)[0]
            output.append(y)
        return output

    def reset(self, mask=None):
        for name, module in self.conv2.named_modules():
            if hasattr(module, "reset"):
                module.reset(mask)

    @torch.jit.export
    def reset_all(self):
        for module in self.conv2:
            module.reset_all()



class Resnet_50(nn.Module):

    def __init__(self, cin=1, base=16, cout=256):
        print('ResNet-50')
        super(Resnet_50, self).__init__()
        self.levels = 5
        self.base = base
        self.cout = cout
        self.in_channels = 64
        print("Hello")
        self.conv1 = SequenceWise(nn.Sequential(
            ConvLayer(cin, 64, kernel_size=7, stride=2, padding=3,bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=3,stride=2,padding=1),
            self._make_layer(Bottleneck, 3, inter_channels=64, stride=1),
            self._make_layer(Bottleneck, 4, inter_channels=128, stride=2),
            self._make_layer(Bottleneck, 6, inter_channels=256, stride=2),
            self._make_layer(Bottleneck, 3, inter_channels=512, stride=2)
        ))
        self.conv2 = nn.ModuleList()
        self.conv2.append(ConvRNN(64 * 32, cout, stride=2))
        for i in range(4):
            self.conv2.append(ConvRNN(cout, cout, stride=2))
    
    def _make_layer(self, block, num_residual_blocks, inter_channels, stride):
        identity_downsample = None
        layers = []
        if stride != 1 or self.in_channels != inter_channels * 4:
            identity_downsample = nn.Sequential(nn.Conv2d(self.in_channels,inter_channels*4,kernel_size=1,
                stride=stride,
                bias=False
                ),
                nn.BatchNorm2d(inter_channels * 4),)
        layers.append(
            block(self.in_channels, inter_channels, identity_downsample, stride)
        )

        # The expansion size is always 4 for ResNet 50,101,152
        self.in_channels = inter_channels * 4

        for i in range(num_residual_blocks - 1):
            layers.append(block(self.in_channels, inter_channels))

        return nn.Sequential(*layers)

    def forward(self, x):
        x = self.conv1(x)
        output = []
        for conv in self.conv2:
            x = conv(x)
            y = time_to_batch(x)[0]
            output.append(y)
        return output

    def reset(self, mask=None):
        for name, module in self.conv2.named_modules():
            if hasattr(module, "reset"):
                module.reset(mask)

    @torch.jit.export
    def reset_all(self):
        for module in self.conv2:
            module.reset_all()

