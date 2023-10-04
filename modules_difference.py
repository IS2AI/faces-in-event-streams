# Please navigate to original modules.py and add the following code after line 178 of the original file

class Bottleneck(nn.Module):
  
    def __init__(self, in_channels, inter_channels, identity_downsample=None, stride=1, norm="BatchNorm2d"):
        super(Bottleneck, self).__init__()
        self.expansion=4
        bias = norm == 'none'
        self.in_channels = in_channels
        self.conv1 = ConvLayer(
            in_channels=in_channels,
            out_channels=inter_channels,
            kernel_size=1,
            stride=1,
            padding=0,
            bias=False,
            norm=norm,
        )
        self.conv2 = ConvLayer(
            in_channels=inter_channels,
            out_channels=inter_channels,
            kernel_size=3,
            stride=stride,
            padding=1,
            norm=norm,
            bias=False,
        )
        self.conv3 = ConvLayer(
            in_channels=inter_channels,
            out_channels=inter_channels*self.expansion,
            kernel_size=1,
            stride=1,
            padding=0,
            norm=norm,
            bias=False,
        )

        self.identity_downsample = identity_downsample
        self.stride = stride

    def forward(self, x):
        identity=x.clone()
        out = self.conv1(x)
        out = self.conv2(out)
        out = self.conv3(out)
        if self.identity_downsample is not None:
            identity = self.identity_downsample(identity)
        out += identity
        out = F.relu(out)
        return out
